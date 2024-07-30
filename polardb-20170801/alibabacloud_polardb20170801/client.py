# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_polardb20170801 import models as polardb_20170801_models
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
            'cn-qingdao': 'polardb.aliyuncs.com',
            'cn-beijing': 'polardb.aliyuncs.com',
            'cn-wulanchabu': 'polardb.aliyuncs.com',
            'cn-hangzhou': 'polardb.aliyuncs.com',
            'cn-shanghai': 'polardb.aliyuncs.com',
            'cn-shenzhen': 'polardb.aliyuncs.com',
            'cn-guangzhou': 'polardb.aliyuncs.com',
            'cn-hongkong': 'polardb.aliyuncs.com',
            'cn-hangzhou-finance': 'polardb.aliyuncs.com',
            'cn-shanghai-finance-1': 'polardb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'polardb.aliyuncs.com',
            'cn-north-2-gov-1': 'polardb.aliyuncs.com',
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
            'cn-qingdao-nebula': 'polardb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'polardb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'polardb.aliyuncs.com',
            'cn-shanghai-inner': 'polardb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'polardb.aliyuncs.com',
            'cn-shenzhen-inner': 'polardb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'polardb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'polardb.aliyuncs.com',
            'cn-wuhan': 'polardb.aliyuncs.com',
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
        """
        @summary Cancels scheduled tasks that are not yet started.
        
        @param request: CancelScheduleTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelScheduleTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelScheduleTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CancelScheduleTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_schedule_tasks_with_options_async(
        self,
        request: polardb_20170801_models.CancelScheduleTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CancelScheduleTasksResponse:
        """
        @summary Cancels scheduled tasks that are not yet started.
        
        @param request: CancelScheduleTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelScheduleTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelScheduleTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CancelScheduleTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_schedule_tasks(
        self,
        request: polardb_20170801_models.CancelScheduleTasksRequest,
    ) -> polardb_20170801_models.CancelScheduleTasksResponse:
        """
        @summary Cancels scheduled tasks that are not yet started.
        
        @param request: CancelScheduleTasksRequest
        @return: CancelScheduleTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_schedule_tasks_with_options(request, runtime)

    async def cancel_schedule_tasks_async(
        self,
        request: polardb_20170801_models.CancelScheduleTasksRequest,
    ) -> polardb_20170801_models.CancelScheduleTasksResponse:
        """
        @summary Cancels scheduled tasks that are not yet started.
        
        @param request: CancelScheduleTasksRequest
        @return: CancelScheduleTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_schedule_tasks_with_options_async(request, runtime)

    def check_account_name_with_options(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        """
        @summary Checks whether an account name is valid or unique in a cluster.
        
        @param request: CheckAccountNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccountNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
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
            action='CheckAccountName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckAccountNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_name_with_options_async(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        """
        @summary Checks whether an account name is valid or unique in a cluster.
        
        @param request: CheckAccountNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccountNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
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
            action='CheckAccountName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckAccountNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account_name(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        """
        @summary Checks whether an account name is valid or unique in a cluster.
        
        @param request: CheckAccountNameRequest
        @return: CheckAccountNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_account_name_with_options(request, runtime)

    async def check_account_name_async(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        """
        @summary Checks whether an account name is valid or unique in a cluster.
        
        @param request: CheckAccountNameRequest
        @return: CheckAccountNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_account_name_with_options_async(request, runtime)

    def check_dbname_with_options(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        """
        @summary Checks whether a database name is valid or whether the name is already used by another database in the current cluster.
        
        @param request: CheckDBNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDBNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='CheckDBName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckDBNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_dbname_with_options_async(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        """
        @summary Checks whether a database name is valid or whether the name is already used by another database in the current cluster.
        
        @param request: CheckDBNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDBNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='CheckDBName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckDBNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_dbname(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        """
        @summary Checks whether a database name is valid or whether the name is already used by another database in the current cluster.
        
        @param request: CheckDBNameRequest
        @return: CheckDBNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_with_options(request, runtime)

    async def check_dbname_async(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        """
        @summary Checks whether a database name is valid or whether the name is already used by another database in the current cluster.
        
        @param request: CheckDBNameRequest
        @return: CheckDBNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_dbname_with_options_async(request, runtime)

    def check_kmsauthorized_with_options(
        self,
        request: polardb_20170801_models.CheckKMSAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckKMSAuthorizedResponse:
        """
        @summary Queries whether the cluster is authorized to use Key Management Service (KMS).
        
        @param request: CheckKMSAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckKMSAuthorizedResponse
        """
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
        if not UtilClient.is_unset(request.tderegion):
            query['TDERegion'] = request.tderegion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckKMSAuthorized',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckKMSAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_kmsauthorized_with_options_async(
        self,
        request: polardb_20170801_models.CheckKMSAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckKMSAuthorizedResponse:
        """
        @summary Queries whether the cluster is authorized to use Key Management Service (KMS).
        
        @param request: CheckKMSAuthorizedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckKMSAuthorizedResponse
        """
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
        if not UtilClient.is_unset(request.tderegion):
            query['TDERegion'] = request.tderegion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckKMSAuthorized',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckKMSAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_kmsauthorized(
        self,
        request: polardb_20170801_models.CheckKMSAuthorizedRequest,
    ) -> polardb_20170801_models.CheckKMSAuthorizedResponse:
        """
        @summary Queries whether the cluster is authorized to use Key Management Service (KMS).
        
        @param request: CheckKMSAuthorizedRequest
        @return: CheckKMSAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_kmsauthorized_with_options(request, runtime)

    async def check_kmsauthorized_async(
        self,
        request: polardb_20170801_models.CheckKMSAuthorizedRequest,
    ) -> polardb_20170801_models.CheckKMSAuthorizedResponse:
        """
        @summary Queries whether the cluster is authorized to use Key Management Service (KMS).
        
        @param request: CheckKMSAuthorizedRequest
        @return: CheckKMSAuthorizedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_kmsauthorized_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: polardb_20170801_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role (SLR) is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='CheckServiceLinkedRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: polardb_20170801_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role (SLR) is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='CheckServiceLinkedRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: polardb_20170801_models.CheckServiceLinkedRoleRequest,
    ) -> polardb_20170801_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role (SLR) is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: polardb_20170801_models.CheckServiceLinkedRoleRequest,
    ) -> polardb_20170801_models.CheckServiceLinkedRoleResponse:
        """
        @summary Checks whether a service-linked role (SLR) is created.
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def close_aitask_with_options(
        self,
        request: polardb_20170801_models.CloseAITaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CloseAITaskResponse:
        """
        @summary 关闭DB4AI
        
        @param request: CloseAITaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseAITaskResponse
        """
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
            action='CloseAITask',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CloseAITaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_aitask_with_options_async(
        self,
        request: polardb_20170801_models.CloseAITaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CloseAITaskResponse:
        """
        @summary 关闭DB4AI
        
        @param request: CloseAITaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseAITaskResponse
        """
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
            action='CloseAITask',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CloseAITaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_aitask(
        self,
        request: polardb_20170801_models.CloseAITaskRequest,
    ) -> polardb_20170801_models.CloseAITaskResponse:
        """
        @summary 关闭DB4AI
        
        @param request: CloseAITaskRequest
        @return: CloseAITaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_aitask_with_options(request, runtime)

    async def close_aitask_async(
        self,
        request: polardb_20170801_models.CloseAITaskRequest,
    ) -> polardb_20170801_models.CloseAITaskResponse:
        """
        @summary 关闭DB4AI
        
        @param request: CloseAITaskRequest
        @return: CloseAITaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_aitask_with_options_async(request, runtime)

    def close_dbcluster_migration_with_options(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        """
        @summary Cancels or completes the migration task that upgrades an RDS cluster to a PolarDB cluster.
        
        @description    You can call this operation to cancel the migration task before data migration.
        You can call this operation to perform the migration task after data migration.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: CloseDBClusterMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseDBClusterMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.continue_enable_binlog):
            query['ContinueEnableBinlog'] = request.continue_enable_binlog
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
            action='CloseDBClusterMigration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CloseDBClusterMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_dbcluster_migration_with_options_async(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        """
        @summary Cancels or completes the migration task that upgrades an RDS cluster to a PolarDB cluster.
        
        @description    You can call this operation to cancel the migration task before data migration.
        You can call this operation to perform the migration task after data migration.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: CloseDBClusterMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseDBClusterMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.continue_enable_binlog):
            query['ContinueEnableBinlog'] = request.continue_enable_binlog
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
            action='CloseDBClusterMigration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CloseDBClusterMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_dbcluster_migration(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        """
        @summary Cancels or completes the migration task that upgrades an RDS cluster to a PolarDB cluster.
        
        @description    You can call this operation to cancel the migration task before data migration.
        You can call this operation to perform the migration task after data migration.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: CloseDBClusterMigrationRequest
        @return: CloseDBClusterMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_dbcluster_migration_with_options(request, runtime)

    async def close_dbcluster_migration_async(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        """
        @summary Cancels or completes the migration task that upgrades an RDS cluster to a PolarDB cluster.
        
        @description    You can call this operation to cancel the migration task before data migration.
        You can call this operation to perform the migration task after data migration.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: CloseDBClusterMigrationRequest
        @return: CloseDBClusterMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_dbcluster_migration_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateAccountResponse:
        """
        @summary Creates a database account for a PolarDB cluster.
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priv_for_all_db):
            query['PrivForAllDB'] = request.priv_for_all_db
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateAccountResponse:
        """
        @summary Creates a database account for a PolarDB cluster.
        
        @param request: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priv_for_all_db):
            query['PrivForAllDB'] = request.priv_for_all_db
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
    ) -> polardb_20170801_models.CreateAccountResponse:
        """
        @summary Creates a database account for a PolarDB cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
    ) -> polardb_20170801_models.CreateAccountResponse:
        """
        @summary Creates a database account for a PolarDB cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateBackupResponse:
        """
        @summary Creates a full snapshot backup for a PolarDB cluster.
        
        @description >
        You can manually create up to three backups for each cluster.
        The `Exceeding the daily backup times of this DB cluster` error message indicates that three manual backups already exist in your cluster. You must delete existing backups before you call this operation to manually create backups. For more information about how to delete backups, see [Delete backups](https://help.aliyun.com/document_detail/98101.html).
        After you call this operation, a backup task is created in the backend. The task may be time-consuming if you want to back up large amounts of data.
        
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='CreateBackup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateBackupResponse:
        """
        @summary Creates a full snapshot backup for a PolarDB cluster.
        
        @description >
        You can manually create up to three backups for each cluster.
        The `Exceeding the daily backup times of this DB cluster` error message indicates that three manual backups already exist in your cluster. You must delete existing backups before you call this operation to manually create backups. For more information about how to delete backups, see [Delete backups](https://help.aliyun.com/document_detail/98101.html).
        After you call this operation, a backup task is created in the backend. The task may be time-consuming if you want to back up large amounts of data.
        
        @param request: CreateBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='CreateBackup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
    ) -> polardb_20170801_models.CreateBackupResponse:
        """
        @summary Creates a full snapshot backup for a PolarDB cluster.
        
        @description >
        You can manually create up to three backups for each cluster.
        The `Exceeding the daily backup times of this DB cluster` error message indicates that three manual backups already exist in your cluster. You must delete existing backups before you call this operation to manually create backups. For more information about how to delete backups, see [Delete backups](https://help.aliyun.com/document_detail/98101.html).
        After you call this operation, a backup task is created in the backend. The task may be time-consuming if you want to back up large amounts of data.
        
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
    ) -> polardb_20170801_models.CreateBackupResponse:
        """
        @summary Creates a full snapshot backup for a PolarDB cluster.
        
        @description >
        You can manually create up to three backups for each cluster.
        The `Exceeding the daily backup times of this DB cluster` error message indicates that three manual backups already exist in your cluster. You must delete existing backups before you call this operation to manually create backups. For more information about how to delete backups, see [Delete backups](https://help.aliyun.com/document_detail/98101.html).
        After you call this operation, a backup task is created in the backend. The task may be time-consuming if you want to back up large amounts of data.
        
        @param request: CreateBackupRequest
        @return: CreateBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_cold_storage_instance_with_options(
        self,
        request: polardb_20170801_models.CreateColdStorageInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateColdStorageInstanceResponse:
        """
        @summary 创建冷存储实例
        
        @param request: CreateColdStorageInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateColdStorageInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cold_storage_instance_description):
            query['ColdStorageInstanceDescription'] = request.cold_storage_instance_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateColdStorageInstance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateColdStorageInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cold_storage_instance_with_options_async(
        self,
        request: polardb_20170801_models.CreateColdStorageInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateColdStorageInstanceResponse:
        """
        @summary 创建冷存储实例
        
        @param request: CreateColdStorageInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateColdStorageInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cold_storage_instance_description):
            query['ColdStorageInstanceDescription'] = request.cold_storage_instance_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateColdStorageInstance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateColdStorageInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cold_storage_instance(
        self,
        request: polardb_20170801_models.CreateColdStorageInstanceRequest,
    ) -> polardb_20170801_models.CreateColdStorageInstanceResponse:
        """
        @summary 创建冷存储实例
        
        @param request: CreateColdStorageInstanceRequest
        @return: CreateColdStorageInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cold_storage_instance_with_options(request, runtime)

    async def create_cold_storage_instance_async(
        self,
        request: polardb_20170801_models.CreateColdStorageInstanceRequest,
    ) -> polardb_20170801_models.CreateColdStorageInstanceResponse:
        """
        @summary 创建冷存储实例
        
        @param request: CreateColdStorageInstanceRequest
        @return: CreateColdStorageInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cold_storage_instance_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        """
        @summary Creates a PolarDB cluster.
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_shut_down):
            query['AllowShutDown'] = request.allow_shut_down
        if not UtilClient.is_unset(request.architecture):
            query['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.clone_data_point):
            query['CloneDataPoint'] = request.clone_data_point
        if not UtilClient.is_unset(request.cluster_network_type):
            query['ClusterNetworkType'] = request.cluster_network_type
        if not UtilClient.is_unset(request.creation_category):
            query['CreationCategory'] = request.creation_category
        if not UtilClient.is_unset(request.creation_option):
            query['CreationOption'] = request.creation_option
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbminor_version):
            query['DBMinorVersion'] = request.dbminor_version
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbnode_num):
            query['DBNodeNum'] = request.dbnode_num
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.default_time_zone):
            query['DefaultTimeZone'] = request.default_time_zone
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.hot_standby_cluster):
            query['HotStandbyCluster'] = request.hot_standby_cluster
        if not UtilClient.is_unset(request.loose_polar_log_bin):
            query['LoosePolarLogBin'] = request.loose_polar_log_bin
        if not UtilClient.is_unset(request.loose_xengine):
            query['LooseXEngine'] = request.loose_xengine
        if not UtilClient.is_unset(request.loose_xengine_use_memory_pct):
            query['LooseXEngineUseMemoryPct'] = request.loose_xengine_use_memory_pct
        if not UtilClient.is_unset(request.lower_case_table_names):
            query['LowerCaseTableNames'] = request.lower_case_table_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.proxy_class):
            query['ProxyClass'] = request.proxy_class
        if not UtilClient.is_unset(request.proxy_type):
            query['ProxyType'] = request.proxy_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.scale_ro_num_max):
            query['ScaleRoNumMax'] = request.scale_ro_num_max
        if not UtilClient.is_unset(request.scale_ro_num_min):
            query['ScaleRoNumMin'] = request.scale_ro_num_min
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.serverless_type):
            query['ServerlessType'] = request.serverless_type
        if not UtilClient.is_unset(request.source_resource_id):
            query['SourceResourceId'] = request.source_resource_id
        if not UtilClient.is_unset(request.standby_az):
            query['StandbyAZ'] = request.standby_az
        if not UtilClient.is_unset(request.storage_auto_scale):
            query['StorageAutoScale'] = request.storage_auto_scale
        if not UtilClient.is_unset(request.storage_pay_type):
            query['StoragePayType'] = request.storage_pay_type
        if not UtilClient.is_unset(request.storage_space):
            query['StorageSpace'] = request.storage_space
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_upper_bound):
            query['StorageUpperBound'] = request.storage_upper_bound
        if not UtilClient.is_unset(request.strict_consistency):
            query['StrictConsistency'] = request.strict_consistency
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        """
        @summary Creates a PolarDB cluster.
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_shut_down):
            query['AllowShutDown'] = request.allow_shut_down
        if not UtilClient.is_unset(request.architecture):
            query['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.clone_data_point):
            query['CloneDataPoint'] = request.clone_data_point
        if not UtilClient.is_unset(request.cluster_network_type):
            query['ClusterNetworkType'] = request.cluster_network_type
        if not UtilClient.is_unset(request.creation_category):
            query['CreationCategory'] = request.creation_category
        if not UtilClient.is_unset(request.creation_option):
            query['CreationOption'] = request.creation_option
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbminor_version):
            query['DBMinorVersion'] = request.dbminor_version
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbnode_num):
            query['DBNodeNum'] = request.dbnode_num
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.default_time_zone):
            query['DefaultTimeZone'] = request.default_time_zone
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.hot_standby_cluster):
            query['HotStandbyCluster'] = request.hot_standby_cluster
        if not UtilClient.is_unset(request.loose_polar_log_bin):
            query['LoosePolarLogBin'] = request.loose_polar_log_bin
        if not UtilClient.is_unset(request.loose_xengine):
            query['LooseXEngine'] = request.loose_xengine
        if not UtilClient.is_unset(request.loose_xengine_use_memory_pct):
            query['LooseXEngineUseMemoryPct'] = request.loose_xengine_use_memory_pct
        if not UtilClient.is_unset(request.lower_case_table_names):
            query['LowerCaseTableNames'] = request.lower_case_table_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not UtilClient.is_unset(request.proxy_class):
            query['ProxyClass'] = request.proxy_class
        if not UtilClient.is_unset(request.proxy_type):
            query['ProxyType'] = request.proxy_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.scale_ro_num_max):
            query['ScaleRoNumMax'] = request.scale_ro_num_max
        if not UtilClient.is_unset(request.scale_ro_num_min):
            query['ScaleRoNumMin'] = request.scale_ro_num_min
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.serverless_type):
            query['ServerlessType'] = request.serverless_type
        if not UtilClient.is_unset(request.source_resource_id):
            query['SourceResourceId'] = request.source_resource_id
        if not UtilClient.is_unset(request.standby_az):
            query['StandbyAZ'] = request.standby_az
        if not UtilClient.is_unset(request.storage_auto_scale):
            query['StorageAutoScale'] = request.storage_auto_scale
        if not UtilClient.is_unset(request.storage_pay_type):
            query['StoragePayType'] = request.storage_pay_type
        if not UtilClient.is_unset(request.storage_space):
            query['StorageSpace'] = request.storage_space
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.storage_upper_bound):
            query['StorageUpperBound'] = request.storage_upper_bound
        if not UtilClient.is_unset(request.strict_consistency):
            query['StrictConsistency'] = request.strict_consistency
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        """
        @summary Creates a PolarDB cluster.
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        """
        @summary Creates a PolarDB cluster.
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbcluster_endpoint_with_options(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        """
        @summary Creates a custom cluster endpoint for a PolarDB cluster.
        
        @param request: CreateDBClusterEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_add_new_nodes):
            query['AutoAddNewNodes'] = request.auto_add_new_nodes
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_description):
            query['DBEndpointDescription'] = request.dbendpoint_description
        if not UtilClient.is_unset(request.endpoint_config):
            query['EndpointConfig'] = request.endpoint_config
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.nodes):
            query['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.polar_scc_timeout_action):
            query['PolarSccTimeoutAction'] = request.polar_scc_timeout_action
        if not UtilClient.is_unset(request.polar_scc_wait_timeout):
            query['PolarSccWaitTimeout'] = request.polar_scc_wait_timeout
        if not UtilClient.is_unset(request.read_write_mode):
            query['ReadWriteMode'] = request.read_write_mode
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scc_mode):
            query['SccMode'] = request.scc_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBClusterEndpoint',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBClusterEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_endpoint_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        """
        @summary Creates a custom cluster endpoint for a PolarDB cluster.
        
        @param request: CreateDBClusterEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_add_new_nodes):
            query['AutoAddNewNodes'] = request.auto_add_new_nodes
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_description):
            query['DBEndpointDescription'] = request.dbendpoint_description
        if not UtilClient.is_unset(request.endpoint_config):
            query['EndpointConfig'] = request.endpoint_config
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not UtilClient.is_unset(request.nodes):
            query['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.polar_scc_timeout_action):
            query['PolarSccTimeoutAction'] = request.polar_scc_timeout_action
        if not UtilClient.is_unset(request.polar_scc_wait_timeout):
            query['PolarSccWaitTimeout'] = request.polar_scc_wait_timeout
        if not UtilClient.is_unset(request.read_write_mode):
            query['ReadWriteMode'] = request.read_write_mode
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scc_mode):
            query['SccMode'] = request.scc_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBClusterEndpoint',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBClusterEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster_endpoint(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        """
        @summary Creates a custom cluster endpoint for a PolarDB cluster.
        
        @param request: CreateDBClusterEndpointRequest
        @return: CreateDBClusterEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_endpoint_with_options(request, runtime)

    async def create_dbcluster_endpoint_async(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        """
        @summary Creates a custom cluster endpoint for a PolarDB cluster.
        
        @param request: CreateDBClusterEndpointRequest
        @return: CreateDBClusterEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_endpoint_with_options_async(request, runtime)

    def create_dbendpoint_address_with_options(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        """
        @summary Creates a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @description > You can create a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @param request: CreateDBEndpointAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.zone_info):
            query['ZoneInfo'] = request.zone_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBEndpointAddress',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbendpoint_address_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        """
        @summary Creates a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @description > You can create a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @param request: CreateDBEndpointAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.zone_info):
            query['ZoneInfo'] = request.zone_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBEndpointAddress',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBEndpointAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbendpoint_address(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        """
        @summary Creates a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @description > You can create a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @param request: CreateDBEndpointAddressRequest
        @return: CreateDBEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbendpoint_address_with_options(request, runtime)

    async def create_dbendpoint_address_async(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        """
        @summary Creates a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @description > You can create a public endpoint for the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        
        @param request: CreateDBEndpointAddressRequest
        @return: CreateDBEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbendpoint_address_with_options_async(request, runtime)

    def create_dblink_with_options(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        """
        @summary Creates a database link.
        
        @description A database link can be used to connect two PolarDB for PostgreSQL(Compatible with Oracle) clusters, or connect a PolarDB for PostgreSQL(Compatible with Oracle) cluster to a user-created PostgreSQL database that is hosted on an Elastic Compute Service (ECS) instance. You can use database links to query data across clusters.
        >    You can create up to 10 database links for a cluster.
        >    Each database link connects a source cluster and a destination cluster.
        >    The source cluster and the destination cluster or the destination ECS instance must be located in the same region.
        
        @param request: CreateDBLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dblink_name):
            query['DBLinkName'] = request.dblink_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_dbname):
            query['SourceDBName'] = request.source_dbname
        if not UtilClient.is_unset(request.target_dbaccount):
            query['TargetDBAccount'] = request.target_dbaccount
        if not UtilClient.is_unset(request.target_dbinstance_name):
            query['TargetDBInstanceName'] = request.target_dbinstance_name
        if not UtilClient.is_unset(request.target_dbname):
            query['TargetDBName'] = request.target_dbname
        if not UtilClient.is_unset(request.target_dbpasswd):
            query['TargetDBPasswd'] = request.target_dbpasswd
        if not UtilClient.is_unset(request.target_ip):
            query['TargetIp'] = request.target_ip
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBLink',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dblink_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        """
        @summary Creates a database link.
        
        @description A database link can be used to connect two PolarDB for PostgreSQL(Compatible with Oracle) clusters, or connect a PolarDB for PostgreSQL(Compatible with Oracle) cluster to a user-created PostgreSQL database that is hosted on an Elastic Compute Service (ECS) instance. You can use database links to query data across clusters.
        >    You can create up to 10 database links for a cluster.
        >    Each database link connects a source cluster and a destination cluster.
        >    The source cluster and the destination cluster or the destination ECS instance must be located in the same region.
        
        @param request: CreateDBLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dblink_name):
            query['DBLinkName'] = request.dblink_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_dbname):
            query['SourceDBName'] = request.source_dbname
        if not UtilClient.is_unset(request.target_dbaccount):
            query['TargetDBAccount'] = request.target_dbaccount
        if not UtilClient.is_unset(request.target_dbinstance_name):
            query['TargetDBInstanceName'] = request.target_dbinstance_name
        if not UtilClient.is_unset(request.target_dbname):
            query['TargetDBName'] = request.target_dbname
        if not UtilClient.is_unset(request.target_dbpasswd):
            query['TargetDBPasswd'] = request.target_dbpasswd
        if not UtilClient.is_unset(request.target_ip):
            query['TargetIp'] = request.target_ip
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBLink',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dblink(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        """
        @summary Creates a database link.
        
        @description A database link can be used to connect two PolarDB for PostgreSQL(Compatible with Oracle) clusters, or connect a PolarDB for PostgreSQL(Compatible with Oracle) cluster to a user-created PostgreSQL database that is hosted on an Elastic Compute Service (ECS) instance. You can use database links to query data across clusters.
        >    You can create up to 10 database links for a cluster.
        >    Each database link connects a source cluster and a destination cluster.
        >    The source cluster and the destination cluster or the destination ECS instance must be located in the same region.
        
        @param request: CreateDBLinkRequest
        @return: CreateDBLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dblink_with_options(request, runtime)

    async def create_dblink_async(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        """
        @summary Creates a database link.
        
        @description A database link can be used to connect two PolarDB for PostgreSQL(Compatible with Oracle) clusters, or connect a PolarDB for PostgreSQL(Compatible with Oracle) cluster to a user-created PostgreSQL database that is hosted on an Elastic Compute Service (ECS) instance. You can use database links to query data across clusters.
        >    You can create up to 10 database links for a cluster.
        >    Each database link connects a source cluster and a destination cluster.
        >    The source cluster and the destination cluster or the destination ECS instance must be located in the same region.
        
        @param request: CreateDBLinkRequest
        @return: CreateDBLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dblink_with_options_async(request, runtime)

    def create_dbnodes_with_options(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        """
        @summary Adds a read-only node to a PolarDB cluster.
        
        @param request: CreateDBNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode):
            query['DBNode'] = request.dbnode
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not UtilClient.is_unset(request.endpoint_bind_list):
            query['EndpointBindList'] = request.endpoint_bind_list
        if not UtilClient.is_unset(request.imci_switch):
            query['ImciSwitch'] = request.imci_switch
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBNodes',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbnodes_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        """
        @summary Adds a read-only node to a PolarDB cluster.
        
        @param request: CreateDBNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode):
            query['DBNode'] = request.dbnode
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not UtilClient.is_unset(request.endpoint_bind_list):
            query['EndpointBindList'] = request.endpoint_bind_list
        if not UtilClient.is_unset(request.imci_switch):
            query['ImciSwitch'] = request.imci_switch
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBNodes',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDBNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbnodes(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        """
        @summary Adds a read-only node to a PolarDB cluster.
        
        @param request: CreateDBNodesRequest
        @return: CreateDBNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbnodes_with_options(request, runtime)

    async def create_dbnodes_async(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        """
        @summary Adds a read-only node to a PolarDB cluster.
        
        @param request: CreateDBNodesRequest
        @return: CreateDBNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbnodes_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        """
        @summary Creates a database for a PolarDB cluster.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The cluster is in the Running state.
        The cluster is unlocked.
        
        @param request: CreateDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.character_set_name):
            query['CharacterSetName'] = request.character_set_name
        if not UtilClient.is_unset(request.collate):
            query['Collate'] = request.collate
        if not UtilClient.is_unset(request.ctype):
            query['Ctype'] = request.ctype
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbdescription):
            query['DBDescription'] = request.dbdescription
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='CreateDatabase',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        """
        @summary Creates a database for a PolarDB cluster.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The cluster is in the Running state.
        The cluster is unlocked.
        
        @param request: CreateDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.character_set_name):
            query['CharacterSetName'] = request.character_set_name
        if not UtilClient.is_unset(request.collate):
            query['Collate'] = request.collate
        if not UtilClient.is_unset(request.ctype):
            query['Ctype'] = request.ctype
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbdescription):
            query['DBDescription'] = request.dbdescription
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='CreateDatabase',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        """
        @summary Creates a database for a PolarDB cluster.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The cluster is in the Running state.
        The cluster is unlocked.
        
        @param request: CreateDatabaseRequest
        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        """
        @summary Creates a database for a PolarDB cluster.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The cluster is in the Running state.
        The cluster is unlocked.
        
        @param request: CreateDatabaseRequest
        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_global_database_network_with_options(
        self,
        request: polardb_20170801_models.CreateGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateGlobalDatabaseNetworkResponse:
        """
        @summary Creates a global database network (GDN).
        
        @description >  A cluster belongs to only one GDN.
        
        @param request: CreateGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.gdndescription):
            query['GDNDescription'] = request.gdndescription
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateGlobalDatabaseNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_database_network_with_options_async(
        self,
        request: polardb_20170801_models.CreateGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateGlobalDatabaseNetworkResponse:
        """
        @summary Creates a global database network (GDN).
        
        @description >  A cluster belongs to only one GDN.
        
        @param request: CreateGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.gdndescription):
            query['GDNDescription'] = request.gdndescription
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateGlobalDatabaseNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_database_network(
        self,
        request: polardb_20170801_models.CreateGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.CreateGlobalDatabaseNetworkResponse:
        """
        @summary Creates a global database network (GDN).
        
        @description >  A cluster belongs to only one GDN.
        
        @param request: CreateGlobalDatabaseNetworkRequest
        @return: CreateGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_global_database_network_with_options(request, runtime)

    async def create_global_database_network_async(
        self,
        request: polardb_20170801_models.CreateGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.CreateGlobalDatabaseNetworkResponse:
        """
        @summary Creates a global database network (GDN).
        
        @description >  A cluster belongs to only one GDN.
        
        @param request: CreateGlobalDatabaseNetworkRequest
        @return: CreateGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_global_database_network_with_options_async(request, runtime)

    def create_global_security_ipgroup_with_options(
        self,
        request: polardb_20170801_models.CreateGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_security_ipgroup_with_options_async(
        self,
        request: polardb_20170801_models.CreateGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_security_ipgroup(
        self,
        request: polardb_20170801_models.CreateGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @return: CreateGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_global_security_ipgroup_with_options(request, runtime)

    async def create_global_security_ipgroup_async(
        self,
        request: polardb_20170801_models.CreateGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.CreateGlobalSecurityIPGroupResponse:
        """
        @summary Creates a global IP whitelist template.
        
        @param request: CreateGlobalSecurityIPGroupRequest
        @return: CreateGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_global_security_ipgroup_with_options_async(request, runtime)

    def create_parameter_group_with_options(
        self,
        request: polardb_20170801_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateParameterGroupResponse:
        """
        @summary Creates a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > You can call this operation only on a PolarDB for MySQL cluster.
        
        @param request: CreateParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParameterGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parameter_group_with_options_async(
        self,
        request: polardb_20170801_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateParameterGroupResponse:
        """
        @summary Creates a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > You can call this operation only on a PolarDB for MySQL cluster.
        
        @param request: CreateParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_desc):
            query['ParameterGroupDesc'] = request.parameter_group_desc
        if not UtilClient.is_unset(request.parameter_group_name):
            query['ParameterGroupName'] = request.parameter_group_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParameterGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parameter_group(
        self,
        request: polardb_20170801_models.CreateParameterGroupRequest,
    ) -> polardb_20170801_models.CreateParameterGroupResponse:
        """
        @summary Creates a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > You can call this operation only on a PolarDB for MySQL cluster.
        
        @param request: CreateParameterGroupRequest
        @return: CreateParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    async def create_parameter_group_async(
        self,
        request: polardb_20170801_models.CreateParameterGroupRequest,
    ) -> polardb_20170801_models.CreateParameterGroupResponse:
        """
        @summary Creates a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > You can call this operation only on a PolarDB for MySQL cluster.
        
        @param request: CreateParameterGroupRequest
        @return: CreateParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_parameter_group_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: polardb_20170801_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role (SLR).
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='CreateServiceLinkedRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: polardb_20170801_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role (SLR).
        
        @param request: CreateServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='CreateServiceLinkedRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: polardb_20170801_models.CreateServiceLinkedRoleRequest,
    ) -> polardb_20170801_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role (SLR).
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: polardb_20170801_models.CreateServiceLinkedRoleRequest,
    ) -> polardb_20170801_models.CreateServiceLinkedRoleResponse:
        """
        @summary Creates a service-linked role (SLR).
        
        @param request: CreateServiceLinkedRoleRequest
        @return: CreateServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def create_storage_plan_with_options(
        self,
        request: polardb_20170801_models.CreateStoragePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateStoragePlanResponse:
        """
        @summary Purchases a storage plan.
        
        @param request: CreateStoragePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoragePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_class):
            query['StorageClass'] = request.storage_class
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStoragePlan',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateStoragePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_plan_with_options_async(
        self,
        request: polardb_20170801_models.CreateStoragePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateStoragePlanResponse:
        """
        @summary Purchases a storage plan.
        
        @param request: CreateStoragePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoragePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_class):
            query['StorageClass'] = request.storage_class
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStoragePlan',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.CreateStoragePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_plan(
        self,
        request: polardb_20170801_models.CreateStoragePlanRequest,
    ) -> polardb_20170801_models.CreateStoragePlanResponse:
        """
        @summary Purchases a storage plan.
        
        @param request: CreateStoragePlanRequest
        @return: CreateStoragePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_storage_plan_with_options(request, runtime)

    async def create_storage_plan_async(
        self,
        request: polardb_20170801_models.CreateStoragePlanRequest,
    ) -> polardb_20170801_models.CreateStoragePlanResponse:
        """
        @summary Purchases a storage plan.
        
        @param request: CreateStoragePlanRequest
        @return: CreateStoragePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_storage_plan_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        """
        @summary Deletes a database account for a PolarDB cluster.
        
        @description > Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
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
            action='DeleteAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        """
        @summary Deletes a database account for a PolarDB cluster.
        
        @description > Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
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
            action='DeleteAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        """
        @summary Deletes a database account for a PolarDB cluster.
        
        @description > Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        """
        @summary Deletes a database account for a PolarDB cluster.
        
        @description > Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backup_with_options(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        """
        @summary Deletes the backup sets of a PolarDB cluster.
        
        @description Before you call this operation, make sure that the cluster meets the following requirements:
        The cluster is in the Running state.
        The backup sets are in the Success state.
        >    You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the status of backup sets.
        >   After you delete the backup set file, the storage space that is occupied by the file is released. The released storage space is smaller than the size of the file because your snapshots share some data blocks
        
        @param request: DeleteBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
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
            action='DeleteBackup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        """
        @summary Deletes the backup sets of a PolarDB cluster.
        
        @description Before you call this operation, make sure that the cluster meets the following requirements:
        The cluster is in the Running state.
        The backup sets are in the Success state.
        >    You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the status of backup sets.
        >   After you delete the backup set file, the storage space that is occupied by the file is released. The released storage space is smaller than the size of the file because your snapshots share some data blocks
        
        @param request: DeleteBackupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
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
            action='DeleteBackup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        """
        @summary Deletes the backup sets of a PolarDB cluster.
        
        @description Before you call this operation, make sure that the cluster meets the following requirements:
        The cluster is in the Running state.
        The backup sets are in the Success state.
        >    You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the status of backup sets.
        >   After you delete the backup set file, the storage space that is occupied by the file is released. The released storage space is smaller than the size of the file because your snapshots share some data blocks
        
        @param request: DeleteBackupRequest
        @return: DeleteBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    async def delete_backup_async(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        """
        @summary Deletes the backup sets of a PolarDB cluster.
        
        @description Before you call this operation, make sure that the cluster meets the following requirements:
        The cluster is in the Running state.
        The backup sets are in the Success state.
        >    You can call the [DescribeBackups](https://help.aliyun.com/document_detail/98102.html) operation to query the status of backup sets.
        >   After you delete the backup set file, the storage space that is occupied by the file is released. The released storage space is smaller than the size of the file because your snapshots share some data blocks
        
        @param request: DeleteBackupRequest
        @return: DeleteBackupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go PolarDB cluster.
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
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
            action='DeleteDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go PolarDB cluster.
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
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
            action='DeleteDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go PolarDB cluster.
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        """
        @summary Releases a pay-as-you-go PolarDB cluster.
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_dbcluster_endpoint_with_options(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        """
        @summary Releases a custom cluster endpoint of a PolarDB cluster.
        
        @param request: DeleteDBClusterEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
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
            action='DeleteDBClusterEndpoint',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBClusterEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_endpoint_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        """
        @summary Releases a custom cluster endpoint of a PolarDB cluster.
        
        @param request: DeleteDBClusterEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
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
            action='DeleteDBClusterEndpoint',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBClusterEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster_endpoint(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        """
        @summary Releases a custom cluster endpoint of a PolarDB cluster.
        
        @param request: DeleteDBClusterEndpointRequest
        @return: DeleteDBClusterEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_endpoint_with_options(request, runtime)

    async def delete_dbcluster_endpoint_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        """
        @summary Releases a custom cluster endpoint of a PolarDB cluster.
        
        @param request: DeleteDBClusterEndpointRequest
        @return: DeleteDBClusterEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_endpoint_with_options_async(request, runtime)

    def delete_dbendpoint_address_with_options(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        """
        @summary Releases the public endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, and custom cluster endpoint.
        
        @description >    You can delete a public-facing or classic network endpoint of the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        >    Classic network endpoints are supported only on the China site (aliyun.com). Therefore, you do not need to delete classic network endpoints on the International site (alibabacloud.com).
        
        @param request: DeleteDBEndpointAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
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
            action='DeleteDBEndpointAddress',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbendpoint_address_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        """
        @summary Releases the public endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, and custom cluster endpoint.
        
        @description >    You can delete a public-facing or classic network endpoint of the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        >    Classic network endpoints are supported only on the China site (aliyun.com). Therefore, you do not need to delete classic network endpoints on the International site (alibabacloud.com).
        
        @param request: DeleteDBEndpointAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
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
            action='DeleteDBEndpointAddress',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBEndpointAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbendpoint_address(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        """
        @summary Releases the public endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, and custom cluster endpoint.
        
        @description >    You can delete a public-facing or classic network endpoint of the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        >    Classic network endpoints are supported only on the China site (aliyun.com). Therefore, you do not need to delete classic network endpoints on the International site (alibabacloud.com).
        
        @param request: DeleteDBEndpointAddressRequest
        @return: DeleteDBEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbendpoint_address_with_options(request, runtime)

    async def delete_dbendpoint_address_async(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        """
        @summary Releases the public endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, and custom cluster endpoint.
        
        @description >    You can delete a public-facing or classic network endpoint of the primary endpoint, the default cluster endpoint, or a custom cluster endpoint.
        >    Classic network endpoints are supported only on the China site (aliyun.com). Therefore, you do not need to delete classic network endpoints on the International site (alibabacloud.com).
        
        @param request: DeleteDBEndpointAddressRequest
        @return: DeleteDBEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbendpoint_address_with_options_async(request, runtime)

    def delete_dblink_with_options(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        """
        @summary Deletes a database link from a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @param request: DeleteDBLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dblink_name):
            query['DBLinkName'] = request.dblink_name
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
            action='DeleteDBLink',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dblink_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        """
        @summary Deletes a database link from a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @param request: DeleteDBLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBLinkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dblink_name):
            query['DBLinkName'] = request.dblink_name
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
            action='DeleteDBLink',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dblink(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        """
        @summary Deletes a database link from a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @param request: DeleteDBLinkRequest
        @return: DeleteDBLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dblink_with_options(request, runtime)

    async def delete_dblink_async(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        """
        @summary Deletes a database link from a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @param request: DeleteDBLinkRequest
        @return: DeleteDBLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dblink_with_options_async(request, runtime)

    def delete_dbnodes_with_options(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        """
        @summary Deletes a read-only node from a PolarDB cluster.
        
        @param request: DeleteDBNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
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
            action='DeleteDBNodes',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbnodes_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        """
        @summary Deletes a read-only node from a PolarDB cluster.
        
        @param request: DeleteDBNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
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
            action='DeleteDBNodes',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDBNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbnodes(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        """
        @summary Deletes a read-only node from a PolarDB cluster.
        
        @param request: DeleteDBNodesRequest
        @return: DeleteDBNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbnodes_with_options(request, runtime)

    async def delete_dbnodes_async(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        """
        @summary Deletes a read-only node from a PolarDB cluster.
        
        @param request: DeleteDBNodesRequest
        @return: DeleteDBNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbnodes_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        """
        @summary Deletes a database from a PolarDB cluster.
        
        @description >- The cluster must be in the Running state and unlocked. Otherwise, the specified database cannot be deleted.
        >- The delete operation is performed in an asynchronous manner. A long period of time may be required to delete a large database. A success response for this operation only indicates that the request to delete the database is sent. You must query the database to check whether the database is deleted.
        
        @param request: DeleteDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='DeleteDatabase',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        """
        @summary Deletes a database from a PolarDB cluster.
        
        @description >- The cluster must be in the Running state and unlocked. Otherwise, the specified database cannot be deleted.
        >- The delete operation is performed in an asynchronous manner. A long period of time may be required to delete a large database. A success response for this operation only indicates that the request to delete the database is sent. You must query the database to check whether the database is deleted.
        
        @param request: DeleteDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='DeleteDatabase',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        """
        @summary Deletes a database from a PolarDB cluster.
        
        @description >- The cluster must be in the Running state and unlocked. Otherwise, the specified database cannot be deleted.
        >- The delete operation is performed in an asynchronous manner. A long period of time may be required to delete a large database. A success response for this operation only indicates that the request to delete the database is sent. You must query the database to check whether the database is deleted.
        
        @param request: DeleteDatabaseRequest
        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        """
        @summary Deletes a database from a PolarDB cluster.
        
        @description >- The cluster must be in the Running state and unlocked. Otherwise, the specified database cannot be deleted.
        >- The delete operation is performed in an asynchronous manner. A long period of time may be required to delete a large database. A success response for this operation only indicates that the request to delete the database is sent. You must query the database to check whether the database is deleted.
        
        @param request: DeleteDatabaseRequest
        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_global_database_network_with_options(
        self,
        request: polardb_20170801_models.DeleteGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteGlobalDatabaseNetworkResponse:
        """
        @summary Deletes a global database network (GDN).
        
        @description >  You can delete a GDN only when the GDN includes only a primary cluster.
        
        @param request: DeleteGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteGlobalDatabaseNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_database_network_with_options_async(
        self,
        request: polardb_20170801_models.DeleteGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteGlobalDatabaseNetworkResponse:
        """
        @summary Deletes a global database network (GDN).
        
        @description >  You can delete a GDN only when the GDN includes only a primary cluster.
        
        @param request: DeleteGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteGlobalDatabaseNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_database_network(
        self,
        request: polardb_20170801_models.DeleteGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.DeleteGlobalDatabaseNetworkResponse:
        """
        @summary Deletes a global database network (GDN).
        
        @description >  You can delete a GDN only when the GDN includes only a primary cluster.
        
        @param request: DeleteGlobalDatabaseNetworkRequest
        @return: DeleteGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_global_database_network_with_options(request, runtime)

    async def delete_global_database_network_async(
        self,
        request: polardb_20170801_models.DeleteGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.DeleteGlobalDatabaseNetworkResponse:
        """
        @summary Deletes a global database network (GDN).
        
        @description >  You can delete a GDN only when the GDN includes only a primary cluster.
        
        @param request: DeleteGlobalDatabaseNetworkRequest
        @return: DeleteGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_database_network_with_options_async(request, runtime)

    def delete_global_security_ipgroup_with_options(
        self,
        request: polardb_20170801_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_security_ipgroup_with_options_async(
        self,
        request: polardb_20170801_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_security_ipgroup(
        self,
        request: polardb_20170801_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_global_security_ipgroup_with_options(request, runtime)

    async def delete_global_security_ipgroup_async(
        self,
        request: polardb_20170801_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.DeleteGlobalSecurityIPGroupResponse:
        """
        @summary Deletes a global IP whitelist template.
        
        @param request: DeleteGlobalSecurityIPGroupRequest
        @return: DeleteGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_security_ipgroup_with_options_async(request, runtime)

    def delete_masking_rules_with_options(
        self,
        request: polardb_20170801_models.DeleteMaskingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteMaskingRulesResponse:
        """
        @summary Deletes a data masking rule.
        
        @param request: DeleteMaskingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMaskingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMaskingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteMaskingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_masking_rules_with_options_async(
        self,
        request: polardb_20170801_models.DeleteMaskingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteMaskingRulesResponse:
        """
        @summary Deletes a data masking rule.
        
        @param request: DeleteMaskingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMaskingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMaskingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteMaskingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_masking_rules(
        self,
        request: polardb_20170801_models.DeleteMaskingRulesRequest,
    ) -> polardb_20170801_models.DeleteMaskingRulesResponse:
        """
        @summary Deletes a data masking rule.
        
        @param request: DeleteMaskingRulesRequest
        @return: DeleteMaskingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_masking_rules_with_options(request, runtime)

    async def delete_masking_rules_async(
        self,
        request: polardb_20170801_models.DeleteMaskingRulesRequest,
    ) -> polardb_20170801_models.DeleteMaskingRulesResponse:
        """
        @summary Deletes a data masking rule.
        
        @param request: DeleteMaskingRulesRequest
        @return: DeleteMaskingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_masking_rules_with_options_async(request, runtime)

    def delete_parameter_group_with_options(
        self,
        request: polardb_20170801_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template of a PolarDB cluster.
        
        @description You can use parameter templates to manage multiple parameters at a time and quickly apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        >  When you delete a parameter template, the parameter settings that are applied to PolarDB clusters are not affected.
        
        @param request: DeleteParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParameterGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parameter_group_with_options_async(
        self,
        request: polardb_20170801_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template of a PolarDB cluster.
        
        @description You can use parameter templates to manage multiple parameters at a time and quickly apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        >  When you delete a parameter template, the parameter settings that are applied to PolarDB clusters are not affected.
        
        @param request: DeleteParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParameterGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DeleteParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parameter_group(
        self,
        request: polardb_20170801_models.DeleteParameterGroupRequest,
    ) -> polardb_20170801_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template of a PolarDB cluster.
        
        @description You can use parameter templates to manage multiple parameters at a time and quickly apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        >  When you delete a parameter template, the parameter settings that are applied to PolarDB clusters are not affected.
        
        @param request: DeleteParameterGroupRequest
        @return: DeleteParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    async def delete_parameter_group_async(
        self,
        request: polardb_20170801_models.DeleteParameterGroupRequest,
    ) -> polardb_20170801_models.DeleteParameterGroupResponse:
        """
        @summary Deletes a parameter template of a PolarDB cluster.
        
        @description You can use parameter templates to manage multiple parameters at a time and quickly apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        >  When you delete a parameter template, the parameter settings that are applied to PolarDB clusters are not affected.
        
        @param request: DeleteParameterGroupRequest
        @return: DeleteParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_parameter_group_with_options_async(request, runtime)

    def describe_aitask_status_with_options(
        self,
        request: polardb_20170801_models.DescribeAITaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAITaskStatusResponse:
        """
        @summary Queries the state of the PolarDB for AI feature for a cluster.
        
        @param request: DescribeAITaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAITaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAITaskStatus',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeAITaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aitask_status_with_options_async(
        self,
        request: polardb_20170801_models.DescribeAITaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAITaskStatusResponse:
        """
        @summary Queries the state of the PolarDB for AI feature for a cluster.
        
        @param request: DescribeAITaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAITaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAITaskStatus',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeAITaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aitask_status(
        self,
        request: polardb_20170801_models.DescribeAITaskStatusRequest,
    ) -> polardb_20170801_models.DescribeAITaskStatusResponse:
        """
        @summary Queries the state of the PolarDB for AI feature for a cluster.
        
        @param request: DescribeAITaskStatusRequest
        @return: DescribeAITaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_aitask_status_with_options(request, runtime)

    async def describe_aitask_status_async(
        self,
        request: polardb_20170801_models.DescribeAITaskStatusRequest,
    ) -> polardb_20170801_models.DescribeAITaskStatusResponse:
        """
        @summary Queries the state of the PolarDB for AI feature for a cluster.
        
        @param request: DescribeAITaskStatusRequest
        @return: DescribeAITaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_aitask_status_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        """
        @summary Queries information about a database account of a PolarDB cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        """
        @summary Queries information about a database account of a PolarDB cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        """
        @summary Queries information about a database account of a PolarDB cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        """
        @summary Queries information about a database account of a PolarDB cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_auto_renew_attribute_with_options(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoRenewAttribute',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_renew_attribute_with_options_async(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoRenewAttribute',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_renew_attribute(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @return: DescribeAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_renew_attribute_with_options(request, runtime)

    async def describe_auto_renew_attribute_async(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        """
        @summary Queries the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: DescribeAutoRenewAttributeRequest
        @return: DescribeAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_renew_attribute_with_options_async(request, runtime)

    def describe_backup_logs_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        """
        @summary Queries backup logs and the URLs to download the backup logs.
        
        @param request: DescribeBackupLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_region):
            query['BackupRegion'] = request.backup_region
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
            action='DescribeBackupLogs',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_logs_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        """
        @summary Queries backup logs and the URLs to download the backup logs.
        
        @param request: DescribeBackupLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_region):
            query['BackupRegion'] = request.backup_region
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
            action='DescribeBackupLogs',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_logs(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        """
        @summary Queries backup logs and the URLs to download the backup logs.
        
        @param request: DescribeBackupLogsRequest
        @return: DescribeBackupLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_logs_with_options(request, runtime)

    async def describe_backup_logs_async(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        """
        @summary Queries backup logs and the URLs to download the backup logs.
        
        @param request: DescribeBackupLogsRequest
        @return: DescribeBackupLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_logs_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the automatic backup policy of a PolarDB cluster.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the automatic backup policy of a PolarDB cluster.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the automatic backup policy of a PolarDB cluster.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        """
        @summary Queries the automatic backup policy of a PolarDB cluster.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        """
        @summary Queries the backup tasks of a PolarDB cluster.
        
        @param request: DescribeBackupTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
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
            action='DescribeBackupTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        """
        @summary Queries the backup tasks of a PolarDB cluster.
        
        @param request: DescribeBackupTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
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
            action='DescribeBackupTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        """
        @summary Queries the backup tasks of a PolarDB cluster.
        
        @param request: DescribeBackupTasksRequest
        @return: DescribeBackupTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        """
        @summary Queries the backup tasks of a PolarDB cluster.
        
        @param request: DescribeBackupTasksRequest
        @return: DescribeBackupTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        """
        @summary Queries the backup details of a PolarDB cluster.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_region):
            query['BackupRegion'] = request.backup_region
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        """
        @summary Queries the backup details of a PolarDB cluster.
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_region):
            query['BackupRegion'] = request.backup_region
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        """
        @summary Queries the backup details of a PolarDB cluster.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        """
        @summary Queries the backup details of a PolarDB cluster.
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_character_set_name_with_options(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        """
        @summary Queries character sets that are supported by a PolarDB for MySQL cluster.
        
        @param request: DescribeCharacterSetNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCharacterSetNameResponse
        """
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
            action='DescribeCharacterSetName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeCharacterSetNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_character_set_name_with_options_async(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        """
        @summary Queries character sets that are supported by a PolarDB for MySQL cluster.
        
        @param request: DescribeCharacterSetNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCharacterSetNameResponse
        """
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
            action='DescribeCharacterSetName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeCharacterSetNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_character_set_name(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        """
        @summary Queries character sets that are supported by a PolarDB for MySQL cluster.
        
        @param request: DescribeCharacterSetNameRequest
        @return: DescribeCharacterSetNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    async def describe_character_set_name_async(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        """
        @summary Queries character sets that are supported by a PolarDB for MySQL cluster.
        
        @param request: DescribeCharacterSetNameRequest
        @return: DescribeCharacterSetNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_character_set_name_with_options_async(request, runtime)

    def describe_class_list_with_options(
        self,
        request: polardb_20170801_models.DescribeClassListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeClassListResponse:
        """
        @summary Queries the specifications of a cluster.
        
        @param request: DescribeClassListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClassListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.master_ha):
            query['MasterHa'] = request.master_ha
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClassList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeClassListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_class_list_with_options_async(
        self,
        request: polardb_20170801_models.DescribeClassListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeClassListResponse:
        """
        @summary Queries the specifications of a cluster.
        
        @param request: DescribeClassListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClassListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.master_ha):
            query['MasterHa'] = request.master_ha
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClassList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeClassListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_class_list(
        self,
        request: polardb_20170801_models.DescribeClassListRequest,
    ) -> polardb_20170801_models.DescribeClassListResponse:
        """
        @summary Queries the specifications of a cluster.
        
        @param request: DescribeClassListRequest
        @return: DescribeClassListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_class_list_with_options(request, runtime)

    async def describe_class_list_async(
        self,
        request: polardb_20170801_models.DescribeClassListRequest,
    ) -> polardb_20170801_models.DescribeClassListResponse:
        """
        @summary Queries the specifications of a cluster.
        
        @param request: DescribeClassListRequest
        @return: DescribeClassListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_class_list_with_options_async(request, runtime)

    def describe_dbcluster_access_whitelist_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        """
        @summary Queries the IP address whitelists and security groups of a PolarDB cluster.
        
        @param request: DescribeDBClusterAccessWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAccessWhitelistResponse
        """
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
            action='DescribeDBClusterAccessWhitelist',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_access_whitelist_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        """
        @summary Queries the IP address whitelists and security groups of a PolarDB cluster.
        
        @param request: DescribeDBClusterAccessWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAccessWhitelistResponse
        """
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
            action='DescribeDBClusterAccessWhitelist',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_access_whitelist(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        """
        @summary Queries the IP address whitelists and security groups of a PolarDB cluster.
        
        @param request: DescribeDBClusterAccessWhitelistRequest
        @return: DescribeDBClusterAccessWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_whitelist_with_options(request, runtime)

    async def describe_dbcluster_access_whitelist_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        """
        @summary Queries the IP address whitelists and security groups of a PolarDB cluster.
        
        @param request: DescribeDBClusterAccessWhitelistRequest
        @return: DescribeDBClusterAccessWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_access_whitelist_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries information about a PolarDB cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterAttribute',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries information about a PolarDB cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterAttribute',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries information about a PolarDB cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        """
        @summary Queries information about a PolarDB cluster.
        
        @param request: DescribeDBClusterAttributeRequest
        @return: DescribeDBClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_audit_log_collector_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        """
        @summary Describe SQL collector for a PolarDB cluster. Features related to SQL collector include audit log and SQL Explorer.
        
        @param request: DescribeDBClusterAuditLogCollectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAuditLogCollectorResponse
        """
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
            action='DescribeDBClusterAuditLogCollector',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_audit_log_collector_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        """
        @summary Describe SQL collector for a PolarDB cluster. Features related to SQL collector include audit log and SQL Explorer.
        
        @param request: DescribeDBClusterAuditLogCollectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAuditLogCollectorResponse
        """
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
            action='DescribeDBClusterAuditLogCollector',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_audit_log_collector(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        """
        @summary Describe SQL collector for a PolarDB cluster. Features related to SQL collector include audit log and SQL Explorer.
        
        @param request: DescribeDBClusterAuditLogCollectorRequest
        @return: DescribeDBClusterAuditLogCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_audit_log_collector_with_options(request, runtime)

    async def describe_dbcluster_audit_log_collector_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        """
        @summary Describe SQL collector for a PolarDB cluster. Features related to SQL collector include audit log and SQL Explorer.
        
        @param request: DescribeDBClusterAuditLogCollectorRequest
        @return: DescribeDBClusterAuditLogCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_audit_log_collector_with_options_async(request, runtime)

    def describe_dbcluster_available_resources_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        """
        @summary Queries available resources in a PolarDB cluster.
        
        @param request: DescribeDBClusterAvailableResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAvailableResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAvailableResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_available_resources_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        """
        @summary Queries available resources in a PolarDB cluster.
        
        @param request: DescribeDBClusterAvailableResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterAvailableResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAvailableResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_available_resources(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        """
        @summary Queries available resources in a PolarDB cluster.
        
        @param request: DescribeDBClusterAvailableResourcesRequest
        @return: DescribeDBClusterAvailableResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_available_resources_with_options(request, runtime)

    async def describe_dbcluster_available_resources_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        """
        @summary Queries available resources in a PolarDB cluster.
        
        @param request: DescribeDBClusterAvailableResourcesRequest
        @return: DescribeDBClusterAvailableResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_available_resources_with_options_async(request, runtime)

    def describe_dbcluster_connectivity_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterConnectivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterConnectivityResponse:
        """
        @summary Queries whether the source IP address can access a cluster.
        
        @param request: DescribeDBClusterConnectivityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConnectivityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConnectivity',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_connectivity_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterConnectivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterConnectivityResponse:
        """
        @summary Queries whether the source IP address can access a cluster.
        
        @param request: DescribeDBClusterConnectivityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConnectivityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConnectivity',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterConnectivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_connectivity(
        self,
        request: polardb_20170801_models.DescribeDBClusterConnectivityRequest,
    ) -> polardb_20170801_models.DescribeDBClusterConnectivityResponse:
        """
        @summary Queries whether the source IP address can access a cluster.
        
        @param request: DescribeDBClusterConnectivityRequest
        @return: DescribeDBClusterConnectivityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_connectivity_with_options(request, runtime)

    async def describe_dbcluster_connectivity_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterConnectivityRequest,
    ) -> polardb_20170801_models.DescribeDBClusterConnectivityResponse:
        """
        @summary Queries whether the source IP address can access a cluster.
        
        @param request: DescribeDBClusterConnectivityRequest
        @return: DescribeDBClusterConnectivityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_connectivity_with_options_async(request, runtime)

    def describe_dbcluster_endpoints_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        """
        @summary Queries the endpoints of a PolarDB cluster.
        
        @param request: DescribeDBClusterEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterEndpoints',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_endpoints_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        """
        @summary Queries the endpoints of a PolarDB cluster.
        
        @param request: DescribeDBClusterEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterEndpoints',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_endpoints(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        """
        @summary Queries the endpoints of a PolarDB cluster.
        
        @param request: DescribeDBClusterEndpointsRequest
        @return: DescribeDBClusterEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_endpoints_with_options(request, runtime)

    async def describe_dbcluster_endpoints_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        """
        @summary Queries the endpoints of a PolarDB cluster.
        
        @param request: DescribeDBClusterEndpointsRequest
        @return: DescribeDBClusterEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_endpoints_with_options_async(request, runtime)

    def describe_dbcluster_migration_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        """
        @summary Queries the migration status of PolarDB clusters.
        
        @description    You can call this operation to query the status of data migration from an ApsaraDB RDS instance to a PolarDB cluster. For more information, see [Upgrade ApsaraDB RDS for MySQL to PolarDB for MySQL with one click](https://help.aliyun.com/document_detail/121582.html).
        Before you call this operation, make sure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the **CreationOption** parameter to **MigrationFromRDS**.
        
        @param request: DescribeDBClusterMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterMigrationResponse
        """
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
            action='DescribeDBClusterMigration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_migration_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        """
        @summary Queries the migration status of PolarDB clusters.
        
        @description    You can call this operation to query the status of data migration from an ApsaraDB RDS instance to a PolarDB cluster. For more information, see [Upgrade ApsaraDB RDS for MySQL to PolarDB for MySQL with one click](https://help.aliyun.com/document_detail/121582.html).
        Before you call this operation, make sure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the **CreationOption** parameter to **MigrationFromRDS**.
        
        @param request: DescribeDBClusterMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterMigrationResponse
        """
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
            action='DescribeDBClusterMigration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_migration(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        """
        @summary Queries the migration status of PolarDB clusters.
        
        @description    You can call this operation to query the status of data migration from an ApsaraDB RDS instance to a PolarDB cluster. For more information, see [Upgrade ApsaraDB RDS for MySQL to PolarDB for MySQL with one click](https://help.aliyun.com/document_detail/121582.html).
        Before you call this operation, make sure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the **CreationOption** parameter to **MigrationFromRDS**.
        
        @param request: DescribeDBClusterMigrationRequest
        @return: DescribeDBClusterMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_migration_with_options(request, runtime)

    async def describe_dbcluster_migration_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        """
        @summary Queries the migration status of PolarDB clusters.
        
        @description    You can call this operation to query the status of data migration from an ApsaraDB RDS instance to a PolarDB cluster. For more information, see [Upgrade ApsaraDB RDS for MySQL to PolarDB for MySQL with one click](https://help.aliyun.com/document_detail/121582.html).
        Before you call this operation, make sure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the **CreationOption** parameter to **MigrationFromRDS**.
        
        @param request: DescribeDBClusterMigrationRequest
        @return: DescribeDBClusterMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_migration_with_options_async(request, runtime)

    def describe_dbcluster_monitor_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        """
        @summary Queries the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @param request: DescribeDBClusterMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterMonitorResponse
        """
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
            action='DescribeDBClusterMonitor',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_monitor_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        """
        @summary Queries the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @param request: DescribeDBClusterMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterMonitorResponse
        """
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
            action='DescribeDBClusterMonitor',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_monitor(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        """
        @summary Queries the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @param request: DescribeDBClusterMonitorRequest
        @return: DescribeDBClusterMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_monitor_with_options(request, runtime)

    async def describe_dbcluster_monitor_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        """
        @summary Queries the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @param request: DescribeDBClusterMonitorRequest
        @return: DescribeDBClusterMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_monitor_with_options_async(request, runtime)

    def describe_dbcluster_parameters_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        """
        @summary Queries the parameters of a PolarDB cluster.
        
        @param request: DescribeDBClusterParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_parameters_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        """
        @summary Queries the parameters of a PolarDB cluster.
        
        @param request: DescribeDBClusterParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_parameters(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        """
        @summary Queries the parameters of a PolarDB cluster.
        
        @param request: DescribeDBClusterParametersRequest
        @return: DescribeDBClusterParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_parameters_with_options(request, runtime)

    async def describe_dbcluster_parameters_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        """
        @summary Queries the parameters of a PolarDB cluster.
        
        @param request: DescribeDBClusterParametersRequest
        @return: DescribeDBClusterParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_parameters_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        """
        @summary Queries the performance data of a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbcluster_sslwith_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of a PolarDB cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSSLResponse
        """
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
            action='DescribeDBClusterSSL',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_sslwith_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of a PolarDB cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterSSLResponse
        """
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
            action='DescribeDBClusterSSL',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_ssl(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of a PolarDB cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @return: DescribeDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_sslwith_options(request, runtime)

    async def describe_dbcluster_ssl_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        """
        @summary Queries the Secure Sockets Layer (SSL) settings of a PolarDB cluster.
        
        @param request: DescribeDBClusterSSLRequest
        @return: DescribeDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_sslwith_options_async(request, runtime)

    def describe_dbcluster_serverless_conf_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterServerlessConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterServerlessConfResponse:
        """
        @summary Queries the configurations of a serverless cluster.
        
        @param request: DescribeDBClusterServerlessConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterServerlessConfResponse
        """
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
            action='DescribeDBClusterServerlessConf',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterServerlessConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_serverless_conf_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterServerlessConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterServerlessConfResponse:
        """
        @summary Queries the configurations of a serverless cluster.
        
        @param request: DescribeDBClusterServerlessConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterServerlessConfResponse
        """
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
            action='DescribeDBClusterServerlessConf',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterServerlessConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_serverless_conf(
        self,
        request: polardb_20170801_models.DescribeDBClusterServerlessConfRequest,
    ) -> polardb_20170801_models.DescribeDBClusterServerlessConfResponse:
        """
        @summary Queries the configurations of a serverless cluster.
        
        @param request: DescribeDBClusterServerlessConfRequest
        @return: DescribeDBClusterServerlessConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_serverless_conf_with_options(request, runtime)

    async def describe_dbcluster_serverless_conf_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterServerlessConfRequest,
    ) -> polardb_20170801_models.DescribeDBClusterServerlessConfResponse:
        """
        @summary Queries the configurations of a serverless cluster.
        
        @param request: DescribeDBClusterServerlessConfRequest
        @return: DescribeDBClusterServerlessConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_serverless_conf_with_options_async(request, runtime)

    def describe_dbcluster_tdewith_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        """
        @summary Queries the Transparent Data Encryption (TDE) settings of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterTDEResponse
        """
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
            action='DescribeDBClusterTDE',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_tdewith_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        """
        @summary Queries the Transparent Data Encryption (TDE) settings of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterTDEResponse
        """
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
            action='DescribeDBClusterTDE',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_tde(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        """
        @summary Queries the Transparent Data Encryption (TDE) settings of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterTDERequest
        @return: DescribeDBClusterTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_tdewith_options(request, runtime)

    async def describe_dbcluster_tde_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        """
        @summary Queries the Transparent Data Encryption (TDE) settings of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterTDERequest
        @return: DescribeDBClusterTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_tdewith_options_async(request, runtime)

    def describe_dbcluster_version_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        """
        @summary Queries the information about the database engine version of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterVersion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_version_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        """
        @summary Queries the information about the database engine version of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
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
            action='DescribeDBClusterVersion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClusterVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_version(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        """
        @summary Queries the information about the database engine version of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterVersionRequest
        @return: DescribeDBClusterVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_version_with_options(request, runtime)

    async def describe_dbcluster_version_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        """
        @summary Queries the information about the database engine version of a PolarDB for MySQL cluster.
        
        @param request: DescribeDBClusterVersionRequest
        @return: DescribeDBClusterVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_version_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        """
        @summary Queries PolarDB clusters or the clusters that can be accessed by an authorized RAM user.
        
        @param request: DescribeDBClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.recent_creation_interval):
            query['RecentCreationInterval'] = request.recent_creation_interval
        if not UtilClient.is_unset(request.recent_expiration_interval):
            query['RecentExpirationInterval'] = request.recent_expiration_interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        """
        @summary Queries PolarDB clusters or the clusters that can be accessed by an authorized RAM user.
        
        @param request: DescribeDBClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.describe_type):
            query['DescribeType'] = request.describe_type
        if not UtilClient.is_unset(request.expired):
            query['Expired'] = request.expired
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.recent_creation_interval):
            query['RecentCreationInterval'] = request.recent_creation_interval
        if not UtilClient.is_unset(request.recent_expiration_interval):
            query['RecentExpirationInterval'] = request.recent_expiration_interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        """
        @summary Queries PolarDB clusters or the clusters that can be accessed by an authorized RAM user.
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        """
        @summary Queries PolarDB clusters or the clusters that can be accessed by an authorized RAM user.
        
        @param request: DescribeDBClustersRequest
        @return: DescribeDBClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbclusters_with_backups_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        """
        @summary Queries the information about PolarDB clusters that contain backup sets in a region.
        
        @param request: DescribeDBClustersWithBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersWithBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClustersWithBackups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClustersWithBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_backups_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        """
        @summary Queries the information about PolarDB clusters that contain backup sets in a region.
        
        @param request: DescribeDBClustersWithBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClustersWithBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.is_deleted):
            query['IsDeleted'] = request.is_deleted
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClustersWithBackups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBClustersWithBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters_with_backups(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        """
        @summary Queries the information about PolarDB clusters that contain backup sets in a region.
        
        @param request: DescribeDBClustersWithBackupsRequest
        @return: DescribeDBClustersWithBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_backups_with_options(request, runtime)

    async def describe_dbclusters_with_backups_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        """
        @summary Queries the information about PolarDB clusters that contain backup sets in a region.
        
        @param request: DescribeDBClustersWithBackupsRequest
        @return: DescribeDBClustersWithBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_backups_with_options_async(request, runtime)

    def describe_dbinitialize_variable_with_options(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        """
        @summary Queries the attributes that are supported by a PolarDB for PostgreSQL (Compatible with Oracle) cluster or a PolarDB for PostgreSQL cluster, such as the character sets and collations.
        
        @param request: DescribeDBInitializeVariableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInitializeVariableResponse
        """
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
            action='DescribeDBInitializeVariable',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBInitializeVariableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinitialize_variable_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        """
        @summary Queries the attributes that are supported by a PolarDB for PostgreSQL (Compatible with Oracle) cluster or a PolarDB for PostgreSQL cluster, such as the character sets and collations.
        
        @param request: DescribeDBInitializeVariableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInitializeVariableResponse
        """
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
            action='DescribeDBInitializeVariable',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBInitializeVariableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinitialize_variable(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        """
        @summary Queries the attributes that are supported by a PolarDB for PostgreSQL (Compatible with Oracle) cluster or a PolarDB for PostgreSQL cluster, such as the character sets and collations.
        
        @param request: DescribeDBInitializeVariableRequest
        @return: DescribeDBInitializeVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinitialize_variable_with_options(request, runtime)

    async def describe_dbinitialize_variable_async(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        """
        @summary Queries the attributes that are supported by a PolarDB for PostgreSQL (Compatible with Oracle) cluster or a PolarDB for PostgreSQL cluster, such as the character sets and collations.
        
        @param request: DescribeDBInitializeVariableRequest
        @return: DescribeDBInitializeVariableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinitialize_variable_with_options_async(request, runtime)

    def describe_dblinks_with_options(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        """
        @summary Queries the database links of a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @description > You can query only the database links that use a PolarDB for Oracle cluster as the source.
        
        @param request: DescribeDBLinksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBLinksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dblink_name):
            query['DBLinkName'] = request.dblink_name
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
            action='DescribeDBLinks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBLinksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dblinks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        """
        @summary Queries the database links of a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @description > You can query only the database links that use a PolarDB for Oracle cluster as the source.
        
        @param request: DescribeDBLinksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBLinksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dblink_name):
            query['DBLinkName'] = request.dblink_name
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
            action='DescribeDBLinks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBLinksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dblinks(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        """
        @summary Queries the database links of a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @description > You can query only the database links that use a PolarDB for Oracle cluster as the source.
        
        @param request: DescribeDBLinksRequest
        @return: DescribeDBLinksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dblinks_with_options(request, runtime)

    async def describe_dblinks_async(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        """
        @summary Queries the database links of a PolarDB for PostgreSQL (Compatible with Oracle) cluster.
        
        @description > You can query only the database links that use a PolarDB for Oracle cluster as the source.
        
        @param request: DescribeDBLinksRequest
        @return: DescribeDBLinksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dblinks_with_options_async(request, runtime)

    def describe_dbnode_performance_with_options(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        """
        @summary Queries the performance data of a node in a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBNodePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBNodePerformance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBNodePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbnode_performance_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        """
        @summary Queries the performance data of a node in a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBNodePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBNodePerformance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBNodePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbnode_performance(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        """
        @summary Queries the performance data of a node in a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBNodePerformanceRequest
        @return: DescribeDBNodePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbnode_performance_with_options(request, runtime)

    async def describe_dbnode_performance_async(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        """
        @summary Queries the performance data of a node in a PolarDB cluster.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        >  By default, the monitoring data is collected once every 60 seconds. You can call the [ModifyDBClusterMonitor](https://help.aliyun.com/document_detail/159557.html) operation to set the data collection interval to every 5 seconds.
        
        @param request: DescribeDBNodePerformanceRequest
        @return: DescribeDBNodePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbnode_performance_with_options_async(request, runtime)

    def describe_dbnodes_parameters_with_options(
        self,
        request: polardb_20170801_models.DescribeDBNodesParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBNodesParametersResponse:
        """
        @summary Queries the parameters of a specified node in a cluster.
        
        @param request: DescribeDBNodesParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodesParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
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
            action='DescribeDBNodesParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBNodesParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbnodes_parameters_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBNodesParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBNodesParametersResponse:
        """
        @summary Queries the parameters of a specified node in a cluster.
        
        @param request: DescribeDBNodesParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBNodesParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
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
            action='DescribeDBNodesParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBNodesParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbnodes_parameters(
        self,
        request: polardb_20170801_models.DescribeDBNodesParametersRequest,
    ) -> polardb_20170801_models.DescribeDBNodesParametersResponse:
        """
        @summary Queries the parameters of a specified node in a cluster.
        
        @param request: DescribeDBNodesParametersRequest
        @return: DescribeDBNodesParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbnodes_parameters_with_options(request, runtime)

    async def describe_dbnodes_parameters_async(
        self,
        request: polardb_20170801_models.DescribeDBNodesParametersRequest,
    ) -> polardb_20170801_models.DescribeDBNodesParametersResponse:
        """
        @summary Queries the parameters of a specified node in a cluster.
        
        @param request: DescribeDBNodesParametersRequest
        @return: DescribeDBNodesParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbnodes_parameters_with_options_async(request, runtime)

    def describe_dbproxy_performance_with_options(
        self,
        request: polardb_20170801_models.DescribeDBProxyPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBProxyPerformanceResponse:
        """
        @summary Queries the performance data of PolarProxy.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeDBProxyPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBProxyPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyPerformance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBProxyPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbproxy_performance_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBProxyPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBProxyPerformanceResponse:
        """
        @summary Queries the performance data of PolarProxy.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeDBProxyPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBProxyPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBProxyPerformance',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDBProxyPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbproxy_performance(
        self,
        request: polardb_20170801_models.DescribeDBProxyPerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBProxyPerformanceResponse:
        """
        @summary Queries the performance data of PolarProxy.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeDBProxyPerformanceRequest
        @return: DescribeDBProxyPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_performance_with_options(request, runtime)

    async def describe_dbproxy_performance_async(
        self,
        request: polardb_20170801_models.DescribeDBProxyPerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBProxyPerformanceResponse:
        """
        @summary Queries the performance data of PolarProxy.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeDBProxyPerformanceRequest
        @return: DescribeDBProxyPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbproxy_performance_with_options_async(request, runtime)

    def describe_das_config_with_options(
        self,
        request: polardb_20170801_models.DescribeDasConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDasConfigResponse:
        """
        @summary 查看实例的 DAS 配置
        
        @param request: DescribeDasConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDasConfigResponse
        """
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
            action='DescribeDasConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDasConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_das_config_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDasConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDasConfigResponse:
        """
        @summary 查看实例的 DAS 配置
        
        @param request: DescribeDasConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDasConfigResponse
        """
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
            action='DescribeDasConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDasConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_das_config(
        self,
        request: polardb_20170801_models.DescribeDasConfigRequest,
    ) -> polardb_20170801_models.DescribeDasConfigResponse:
        """
        @summary 查看实例的 DAS 配置
        
        @param request: DescribeDasConfigRequest
        @return: DescribeDasConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_das_config_with_options(request, runtime)

    async def describe_das_config_async(
        self,
        request: polardb_20170801_models.DescribeDasConfigRequest,
    ) -> polardb_20170801_models.DescribeDasConfigResponse:
        """
        @summary 查看实例的 DAS 配置
        
        @param request: DescribeDasConfigRequest
        @return: DescribeDasConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_das_config_with_options_async(request, runtime)

    def describe_databases_with_options(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        """
        @summary Queries the information about databases in a PolarDB cluster.
        
        @param request: DescribeDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_databases_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        """
        @summary Queries the information about databases in a PolarDB cluster.
        
        @param request: DescribeDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_databases(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        """
        @summary Queries the information about databases in a PolarDB cluster.
        
        @param request: DescribeDatabasesRequest
        @return: DescribeDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    async def describe_databases_async(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        """
        @summary Queries the information about databases in a PolarDB cluster.
        
        @param request: DescribeDatabasesRequest
        @return: DescribeDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_databases_with_options_async(request, runtime)

    def describe_detached_backups_with_options(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        """
        @summary Queries the information about the backup sets in a released PolarDB cluster.
        
        @description Before you call this operation, make sure that the PolarDB cluster is in the *Released** state. You must also confirm that the **Retain All Backups Permanently** or **Retain Last Automatic Backup Permanently** backup retention policy takes effect after you release the cluster. If you delete all backup sets after the cluster is released, you cannot use this API operation to query the cluster.
        > You can call the [DescribeDBClusterAttribute](https://help.aliyun.com/document_detail/98181.html) operation to query the cluster status.
        
        @param request: DescribeDetachedBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDetachedBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_region):
            query['BackupRegion'] = request.backup_region
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
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
            action='DescribeDetachedBackups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDetachedBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_detached_backups_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        """
        @summary Queries the information about the backup sets in a released PolarDB cluster.
        
        @description Before you call this operation, make sure that the PolarDB cluster is in the *Released** state. You must also confirm that the **Retain All Backups Permanently** or **Retain Last Automatic Backup Permanently** backup retention policy takes effect after you release the cluster. If you delete all backup sets after the cluster is released, you cannot use this API operation to query the cluster.
        > You can call the [DescribeDBClusterAttribute](https://help.aliyun.com/document_detail/98181.html) operation to query the cluster status.
        
        @param request: DescribeDetachedBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDetachedBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_region):
            query['BackupRegion'] = request.backup_region
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
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
            action='DescribeDetachedBackups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeDetachedBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_detached_backups(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        """
        @summary Queries the information about the backup sets in a released PolarDB cluster.
        
        @description Before you call this operation, make sure that the PolarDB cluster is in the *Released** state. You must also confirm that the **Retain All Backups Permanently** or **Retain Last Automatic Backup Permanently** backup retention policy takes effect after you release the cluster. If you delete all backup sets after the cluster is released, you cannot use this API operation to query the cluster.
        > You can call the [DescribeDBClusterAttribute](https://help.aliyun.com/document_detail/98181.html) operation to query the cluster status.
        
        @param request: DescribeDetachedBackupsRequest
        @return: DescribeDetachedBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    async def describe_detached_backups_async(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        """
        @summary Queries the information about the backup sets in a released PolarDB cluster.
        
        @description Before you call this operation, make sure that the PolarDB cluster is in the *Released** state. You must also confirm that the **Retain All Backups Permanently** or **Retain Last Automatic Backup Permanently** backup retention policy takes effect after you release the cluster. If you delete all backup sets after the cluster is released, you cannot use this API operation to query the cluster.
        > You can call the [DescribeDBClusterAttribute](https://help.aliyun.com/document_detail/98181.html) operation to query the cluster status.
        
        @param request: DescribeDetachedBackupsRequest
        @return: DescribeDetachedBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_detached_backups_with_options_async(request, runtime)

    def describe_global_database_network_with_options(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworkResponse:
        """
        @summary Queries the information about a Global Database Network (GDN).
        
        @param request: DescribeGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalDatabaseNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_database_network_with_options_async(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworkResponse:
        """
        @summary Queries the information about a Global Database Network (GDN).
        
        @param request: DescribeGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalDatabaseNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_database_network(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworkResponse:
        """
        @summary Queries the information about a Global Database Network (GDN).
        
        @param request: DescribeGlobalDatabaseNetworkRequest
        @return: DescribeGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_database_network_with_options(request, runtime)

    async def describe_global_database_network_async(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworkResponse:
        """
        @summary Queries the information about a Global Database Network (GDN).
        
        @param request: DescribeGlobalDatabaseNetworkRequest
        @return: DescribeGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_database_network_with_options_async(request, runtime)

    def describe_global_database_networks_with_options(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        """
        @summary Queries the information about all Global Database Networks (GDNs) that belong to an account.
        
        @param request: DescribeGlobalDatabaseNetworksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDatabaseNetworksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_region):
            query['FilterRegion'] = request.filter_region
        if not UtilClient.is_unset(request.gdndescription):
            query['GDNDescription'] = request.gdndescription
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDatabaseNetworks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_database_networks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        """
        @summary Queries the information about all Global Database Networks (GDNs) that belong to an account.
        
        @param request: DescribeGlobalDatabaseNetworksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalDatabaseNetworksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.filter_region):
            query['FilterRegion'] = request.filter_region
        if not UtilClient.is_unset(request.gdndescription):
            query['GDNDescription'] = request.gdndescription
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalDatabaseNetworks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_database_networks(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        """
        @summary Queries the information about all Global Database Networks (GDNs) that belong to an account.
        
        @param request: DescribeGlobalDatabaseNetworksRequest
        @return: DescribeGlobalDatabaseNetworksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_database_networks_with_options(request, runtime)

    async def describe_global_database_networks_async(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        """
        @summary Queries the information about all Global Database Networks (GDNs) that belong to an account.
        
        @param request: DescribeGlobalDatabaseNetworksRequest
        @return: DescribeGlobalDatabaseNetworksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_database_networks_with_options_async(request, runtime)

    def describe_global_security_ipgroup_with_options(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_with_options_async(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_security_ipgroup_with_options(request, runtime)

    async def describe_global_security_ipgroup_async(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupResponse:
        """
        @summary Queries global IP whitelist templates.
        
        @param request: DescribeGlobalSecurityIPGroupRequest
        @return: DescribeGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_security_ipgroup_with_options_async(request, runtime)

    def describe_global_security_ipgroup_relation_with_options(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the relationship between a cluster and a global IP whitelist template.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroupRelation',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_relation_with_options_async(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the relationship between a cluster and a global IP whitelist template.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGlobalSecurityIPGroupRelation',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup_relation(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the relationship between a cluster and a global IP whitelist template.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_global_security_ipgroup_relation_with_options(request, runtime)

    async def describe_global_security_ipgroup_relation_async(
        self,
        request: polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> polardb_20170801_models.DescribeGlobalSecurityIPGroupRelationResponse:
        """
        @summary Queries the relationship between a cluster and a global IP whitelist template.
        
        @param request: DescribeGlobalSecurityIPGroupRelationRequest
        @return: DescribeGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_security_ipgroup_relation_with_options_async(request, runtime)

    def describe_log_backup_policy_with_options(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        """
        @summary Queries the retention policy of log backups in a PolarDB cluster.
        
        @param request: DescribeLogBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogBackupPolicyResponse
        """
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
            action='DescribeLogBackupPolicy',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeLogBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        """
        @summary Queries the retention policy of log backups in a PolarDB cluster.
        
        @param request: DescribeLogBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogBackupPolicyResponse
        """
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
            action='DescribeLogBackupPolicy',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeLogBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_backup_policy(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        """
        @summary Queries the retention policy of log backups in a PolarDB cluster.
        
        @param request: DescribeLogBackupPolicyRequest
        @return: DescribeLogBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_policy_with_options(request, runtime)

    async def describe_log_backup_policy_async(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        """
        @summary Queries the retention policy of log backups in a PolarDB cluster.
        
        @param request: DescribeLogBackupPolicyRequest
        @return: DescribeLogBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_backup_policy_with_options_async(request, runtime)

    def describe_masking_rules_with_options(
        self,
        request: polardb_20170801_models.DescribeMaskingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeMaskingRulesResponse:
        """
        @summary Queries the data masking rules of a PolarDB cluster or the information about a specified masking rule.
        
        @param request: DescribeMaskingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMaskingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaskingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeMaskingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_masking_rules_with_options_async(
        self,
        request: polardb_20170801_models.DescribeMaskingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeMaskingRulesResponse:
        """
        @summary Queries the data masking rules of a PolarDB cluster or the information about a specified masking rule.
        
        @param request: DescribeMaskingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMaskingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaskingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeMaskingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_masking_rules(
        self,
        request: polardb_20170801_models.DescribeMaskingRulesRequest,
    ) -> polardb_20170801_models.DescribeMaskingRulesResponse:
        """
        @summary Queries the data masking rules of a PolarDB cluster or the information about a specified masking rule.
        
        @param request: DescribeMaskingRulesRequest
        @return: DescribeMaskingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_masking_rules_with_options(request, runtime)

    async def describe_masking_rules_async(
        self,
        request: polardb_20170801_models.DescribeMaskingRulesRequest,
    ) -> polardb_20170801_models.DescribeMaskingRulesResponse:
        """
        @summary Queries the data masking rules of a PolarDB cluster or the information about a specified masking rule.
        
        @param request: DescribeMaskingRulesRequest
        @return: DescribeMaskingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_masking_rules_with_options_async(request, runtime)

    def describe_meta_list_with_options(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        """
        @summary Queries the details of the databases or tables that can be restored.
        
        @param request: DescribeMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.get_db_name):
            query['GetDbName'] = request.get_db_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetaList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meta_list_with_options_async(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        """
        @summary Queries the details of the databases or tables that can be restored.
        
        @param request: DescribeMetaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.get_db_name):
            query['GetDbName'] = request.get_db_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMetaList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meta_list(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        """
        @summary Queries the details of the databases or tables that can be restored.
        
        @param request: DescribeMetaListRequest
        @return: DescribeMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_list_with_options(request, runtime)

    async def describe_meta_list_async(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        """
        @summary Queries the details of the databases or tables that can be restored.
        
        @param request: DescribeMetaListRequest
        @return: DescribeMetaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_meta_list_with_options_async(request, runtime)

    def describe_parameter_group_with_options(
        self,
        request: polardb_20170801_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeParameterGroupResponse:
        """
        @summary Queries the information about a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This parameter is valid only for a PolarDB for MySQL cluster.
        
        @param request: DescribeParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeParameterGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_group_with_options_async(
        self,
        request: polardb_20170801_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeParameterGroupResponse:
        """
        @summary Queries the information about a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This parameter is valid only for a PolarDB for MySQL cluster.
        
        @param request: DescribeParameterGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeParameterGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_group(
        self,
        request: polardb_20170801_models.DescribeParameterGroupRequest,
    ) -> polardb_20170801_models.DescribeParameterGroupResponse:
        """
        @summary Queries the information about a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This parameter is valid only for a PolarDB for MySQL cluster.
        
        @param request: DescribeParameterGroupRequest
        @return: DescribeParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    async def describe_parameter_group_async(
        self,
        request: polardb_20170801_models.DescribeParameterGroupRequest,
    ) -> polardb_20170801_models.DescribeParameterGroupResponse:
        """
        @summary Queries the information about a parameter template.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This parameter is valid only for a PolarDB for MySQL cluster.
        
        @param request: DescribeParameterGroupRequest
        @return: DescribeParameterGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_group_with_options_async(request, runtime)

    def describe_parameter_groups_with_options(
        self,
        request: polardb_20170801_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeParameterGroupsResponse:
        """
        @summary Queries parameter templates that are available in a specified region.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeParameterGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeParameterGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_groups_with_options_async(
        self,
        request: polardb_20170801_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeParameterGroupsResponse:
        """
        @summary Queries parameter templates that are available in a specified region.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeParameterGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterGroups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeParameterGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_groups(
        self,
        request: polardb_20170801_models.DescribeParameterGroupsRequest,
    ) -> polardb_20170801_models.DescribeParameterGroupsResponse:
        """
        @summary Queries parameter templates that are available in a specified region.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeParameterGroupsRequest
        @return: DescribeParameterGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    async def describe_parameter_groups_async(
        self,
        request: polardb_20170801_models.DescribeParameterGroupsRequest,
    ) -> polardb_20170801_models.DescribeParameterGroupsResponse:
        """
        @summary Queries parameter templates that are available in a specified region.
        
        @description You can use parameter templates to manage multiple parameters at a time and apply existing parameters to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeParameterGroupsRequest
        @return: DescribeParameterGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_groups_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: polardb_20170801_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the default parameters in a cluster.
        
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: polardb_20170801_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the default parameters in a cluster.
        
        @param request: DescribeParameterTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParameterTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameterTemplates',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeParameterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: polardb_20170801_models.DescribeParameterTemplatesRequest,
    ) -> polardb_20170801_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the default parameters in a cluster.
        
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: polardb_20170801_models.DescribeParameterTemplatesRequest,
    ) -> polardb_20170801_models.DescribeParameterTemplatesResponse:
        """
        @summary Queries the default parameters in a cluster.
        
        @param request: DescribeParameterTemplatesRequest
        @return: DescribeParameterTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_pending_maintenance_action_with_options(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        """
        @summary Queries the information about a pending event.
        
        @param request: DescribePendingMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePendingMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePendingMaintenanceAction',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribePendingMaintenanceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pending_maintenance_action_with_options_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        """
        @summary Queries the information about a pending event.
        
        @param request: DescribePendingMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePendingMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePendingMaintenanceAction',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribePendingMaintenanceActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pending_maintenance_action(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        """
        @summary Queries the information about a pending event.
        
        @param request: DescribePendingMaintenanceActionRequest
        @return: DescribePendingMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pending_maintenance_action_with_options(request, runtime)

    async def describe_pending_maintenance_action_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        """
        @summary Queries the information about a pending event.
        
        @param request: DescribePendingMaintenanceActionRequest
        @return: DescribePendingMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pending_maintenance_action_with_options_async(request, runtime)

    def describe_pending_maintenance_actions_with_options(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        """
        @summary Queries the numbers of pending events of different task types.
        
        @param request: DescribePendingMaintenanceActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePendingMaintenanceActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePendingMaintenanceActions',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribePendingMaintenanceActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pending_maintenance_actions_with_options_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        """
        @summary Queries the numbers of pending events of different task types.
        
        @param request: DescribePendingMaintenanceActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePendingMaintenanceActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_history):
            query['IsHistory'] = request.is_history
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePendingMaintenanceActions',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribePendingMaintenanceActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pending_maintenance_actions(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        """
        @summary Queries the numbers of pending events of different task types.
        
        @param request: DescribePendingMaintenanceActionsRequest
        @return: DescribePendingMaintenanceActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pending_maintenance_actions_with_options(request, runtime)

    async def describe_pending_maintenance_actions_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        """
        @summary Queries the numbers of pending events of different task types.
        
        @param request: DescribePendingMaintenanceActionsRequest
        @return: DescribePendingMaintenanceActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pending_maintenance_actions_with_options_async(request, runtime)

    def describe_polar_sqlcollector_policy_with_options(
        self,
        request: polardb_20170801_models.DescribePolarSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePolarSQLCollectorPolicyResponse:
        """
        @summary Queries whether the SQL Explorer feature is enabled for the cluster.
        
        @param request: DescribePolarSQLCollectorPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolarSQLCollectorPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolarSQLCollectorPolicy',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribePolarSQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_polar_sqlcollector_policy_with_options_async(
        self,
        request: polardb_20170801_models.DescribePolarSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePolarSQLCollectorPolicyResponse:
        """
        @summary Queries whether the SQL Explorer feature is enabled for the cluster.
        
        @param request: DescribePolarSQLCollectorPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolarSQLCollectorPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolarSQLCollectorPolicy',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribePolarSQLCollectorPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_polar_sqlcollector_policy(
        self,
        request: polardb_20170801_models.DescribePolarSQLCollectorPolicyRequest,
    ) -> polardb_20170801_models.DescribePolarSQLCollectorPolicyResponse:
        """
        @summary Queries whether the SQL Explorer feature is enabled for the cluster.
        
        @param request: DescribePolarSQLCollectorPolicyRequest
        @return: DescribePolarSQLCollectorPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_polar_sqlcollector_policy_with_options(request, runtime)

    async def describe_polar_sqlcollector_policy_async(
        self,
        request: polardb_20170801_models.DescribePolarSQLCollectorPolicyRequest,
    ) -> polardb_20170801_models.DescribePolarSQLCollectorPolicyResponse:
        """
        @summary Queries whether the SQL Explorer feature is enabled for the cluster.
        
        @param request: DescribePolarSQLCollectorPolicyRequest
        @return: DescribePolarSQLCollectorPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_polar_sqlcollector_policy_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        """
        @summary Queries the regions and zones available for PolarDB.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        """
        @summary Queries the regions and zones available for PolarDB.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        """
        @summary Queries the regions and zones available for PolarDB.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        """
        @summary Queries the regions and zones available for PolarDB.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_schedule_tasks_with_options(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        """
        @summary Queries the details of all scheduled tasks.
        
        @param request: DescribeScheduleTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduleTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduleTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeScheduleTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schedule_tasks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        """
        @summary Queries the details of all scheduled tasks.
        
        @param request: DescribeScheduleTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduleTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduleTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeScheduleTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schedule_tasks(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        """
        @summary Queries the details of all scheduled tasks.
        
        @param request: DescribeScheduleTasksRequest
        @return: DescribeScheduleTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_tasks_with_options(request, runtime)

    async def describe_schedule_tasks_async(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        """
        @summary Queries the details of all scheduled tasks.
        
        @param request: DescribeScheduleTasksRequest
        @return: DescribeScheduleTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_schedule_tasks_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sqlhash):
            query['SQLHASH'] = request.sqlhash
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sqlhash):
            query['SQLHASH'] = request.sqlhash
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_logs_with_options(
        self,
        request: polardb_20170801_models.DescribeSlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSlowLogsResponse:
        """
        @summary Queries the statistics about the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeSlowLogs',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeSlowLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_logs_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSlowLogsResponse:
        """
        @summary Queries the statistics about the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='DescribeSlowLogs',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeSlowLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_logs(
        self,
        request: polardb_20170801_models.DescribeSlowLogsRequest,
    ) -> polardb_20170801_models.DescribeSlowLogsResponse:
        """
        @summary Queries the statistics about the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogsRequest
        @return: DescribeSlowLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_logs_with_options(request, runtime)

    async def describe_slow_logs_async(
        self,
        request: polardb_20170801_models.DescribeSlowLogsRequest,
    ) -> polardb_20170801_models.DescribeSlowLogsResponse:
        """
        @summary Queries the statistics about the slow query logs of a PolarDB cluster.
        
        @description > This operation is applicable only to PolarDB for MySQL clusters.
        
        @param request: DescribeSlowLogsRequest
        @return: DescribeSlowLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_logs_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        """
        @summary Queries the details of the tasks that are generated by calling API operations. For example, you can call this operation to view the details of the task when you create a cluster.
        
        @description    You can call this operation to view the details of a task that is generated by a specific API operation or in the console. The system calls the specific API operation when you perform an operation in the console. For example, you can view the details of the task when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation or [create a cluster](https://help.aliyun.com/document_detail/58769.html) in the console.
        You can view the details of tasks that are generated only when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create a cluster and `CreationOption` is not set to `CreateGdnStandby`.
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        """
        @summary Queries the details of the tasks that are generated by calling API operations. For example, you can call this operation to view the details of the task when you create a cluster.
        
        @description    You can call this operation to view the details of a task that is generated by a specific API operation or in the console. The system calls the specific API operation when you perform an operation in the console. For example, you can view the details of the task when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation or [create a cluster](https://help.aliyun.com/document_detail/58769.html) in the console.
        You can view the details of tasks that are generated only when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create a cluster and `CreationOption` is not set to `CreateGdnStandby`.
        
        @param request: DescribeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        """
        @summary Queries the details of the tasks that are generated by calling API operations. For example, you can call this operation to view the details of the task when you create a cluster.
        
        @description    You can call this operation to view the details of a task that is generated by a specific API operation or in the console. The system calls the specific API operation when you perform an operation in the console. For example, you can view the details of the task when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation or [create a cluster](https://help.aliyun.com/document_detail/58769.html) in the console.
        You can view the details of tasks that are generated only when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create a cluster and `CreationOption` is not set to `CreateGdnStandby`.
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        """
        @summary Queries the details of the tasks that are generated by calling API operations. For example, you can call this operation to view the details of the task when you create a cluster.
        
        @description    You can call this operation to view the details of a task that is generated by a specific API operation or in the console. The system calls the specific API operation when you perform an operation in the console. For example, you can view the details of the task when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation or [create a cluster](https://help.aliyun.com/document_detail/58769.html) in the console.
        You can view the details of tasks that are generated only when you call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create a cluster and `CreationOption` is not set to `CreateGdnStandby`.
        
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: polardb_20170801_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the Key Management Service (KMS)-managed customer master keys (CMKs) that are used to encrypt data in a PolarDB cluster.
        
        @param request: DescribeUserEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserEncryptionKeyListResponse
        """
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
        if not UtilClient.is_unset(request.tderegion):
            query['TDERegion'] = request.tderegion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeUserEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: polardb_20170801_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the Key Management Service (KMS)-managed customer master keys (CMKs) that are used to encrypt data in a PolarDB cluster.
        
        @param request: DescribeUserEncryptionKeyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserEncryptionKeyListResponse
        """
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
        if not UtilClient.is_unset(request.tderegion):
            query['TDERegion'] = request.tderegion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeUserEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_encryption_key_list(
        self,
        request: polardb_20170801_models.DescribeUserEncryptionKeyListRequest,
    ) -> polardb_20170801_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the Key Management Service (KMS)-managed customer master keys (CMKs) that are used to encrypt data in a PolarDB cluster.
        
        @param request: DescribeUserEncryptionKeyListRequest
        @return: DescribeUserEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    async def describe_user_encryption_key_list_async(
        self,
        request: polardb_20170801_models.DescribeUserEncryptionKeyListRequest,
    ) -> polardb_20170801_models.DescribeUserEncryptionKeyListResponse:
        """
        @summary Queries the Key Management Service (KMS)-managed customer master keys (CMKs) that are used to encrypt data in a PolarDB cluster.
        
        @param request: DescribeUserEncryptionKeyListRequest
        @return: DescribeUserEncryptionKeyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_encryption_key_list_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: polardb_20170801_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeVSwitchesResponse:
        """
        @summary Queries a vSwitch.
        
        @param request: DescribeVSwitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: polardb_20170801_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeVSwitchesResponse:
        """
        @summary Queries a vSwitch.
        
        @param request: DescribeVSwitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: polardb_20170801_models.DescribeVSwitchesRequest,
    ) -> polardb_20170801_models.DescribeVSwitchesResponse:
        """
        @summary Queries a vSwitch.
        
        @param request: DescribeVSwitchesRequest
        @return: DescribeVSwitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: polardb_20170801_models.DescribeVSwitchesRequest,
    ) -> polardb_20170801_models.DescribeVSwitchesResponse:
        """
        @summary Queries a vSwitch.
        
        @param request: DescribeVSwitchesRequest
        @return: DescribeVSwitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def disable_dbcluster_serverless_with_options(
        self,
        request: polardb_20170801_models.DisableDBClusterServerlessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DisableDBClusterServerlessResponse:
        """
        @summary Disables a stable serverless cluster.
        
        @param request: DisableDBClusterServerlessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDBClusterServerlessResponse
        """
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
            action='DisableDBClusterServerless',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DisableDBClusterServerlessResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_dbcluster_serverless_with_options_async(
        self,
        request: polardb_20170801_models.DisableDBClusterServerlessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DisableDBClusterServerlessResponse:
        """
        @summary Disables a stable serverless cluster.
        
        @param request: DisableDBClusterServerlessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDBClusterServerlessResponse
        """
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
            action='DisableDBClusterServerless',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.DisableDBClusterServerlessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_dbcluster_serverless(
        self,
        request: polardb_20170801_models.DisableDBClusterServerlessRequest,
    ) -> polardb_20170801_models.DisableDBClusterServerlessResponse:
        """
        @summary Disables a stable serverless cluster.
        
        @param request: DisableDBClusterServerlessRequest
        @return: DisableDBClusterServerlessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_dbcluster_serverless_with_options(request, runtime)

    async def disable_dbcluster_serverless_async(
        self,
        request: polardb_20170801_models.DisableDBClusterServerlessRequest,
    ) -> polardb_20170801_models.DisableDBClusterServerlessResponse:
        """
        @summary Disables a stable serverless cluster.
        
        @param request: DisableDBClusterServerlessRequest
        @return: DisableDBClusterServerlessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_dbcluster_serverless_with_options_async(request, runtime)

    def enable_dbcluster_serverless_with_options(
        self,
        request: polardb_20170801_models.EnableDBClusterServerlessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.EnableDBClusterServerlessResponse:
        """
        @summary Enables a stable serverless cluster.
        
        @param request: EnableDBClusterServerlessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDBClusterServerlessResponse
        """
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
        if not UtilClient.is_unset(request.scale_ap_ro_num_max):
            query['ScaleApRoNumMax'] = request.scale_ap_ro_num_max
        if not UtilClient.is_unset(request.scale_ap_ro_num_min):
            query['ScaleApRoNumMin'] = request.scale_ap_ro_num_min
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.scale_ro_num_max):
            query['ScaleRoNumMax'] = request.scale_ro_num_max
        if not UtilClient.is_unset(request.scale_ro_num_min):
            query['ScaleRoNumMin'] = request.scale_ro_num_min
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDBClusterServerless',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.EnableDBClusterServerlessResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_dbcluster_serverless_with_options_async(
        self,
        request: polardb_20170801_models.EnableDBClusterServerlessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.EnableDBClusterServerlessResponse:
        """
        @summary Enables a stable serverless cluster.
        
        @param request: EnableDBClusterServerlessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDBClusterServerlessResponse
        """
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
        if not UtilClient.is_unset(request.scale_ap_ro_num_max):
            query['ScaleApRoNumMax'] = request.scale_ap_ro_num_max
        if not UtilClient.is_unset(request.scale_ap_ro_num_min):
            query['ScaleApRoNumMin'] = request.scale_ap_ro_num_min
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.scale_ro_num_max):
            query['ScaleRoNumMax'] = request.scale_ro_num_max
        if not UtilClient.is_unset(request.scale_ro_num_min):
            query['ScaleRoNumMin'] = request.scale_ro_num_min
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDBClusterServerless',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.EnableDBClusterServerlessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_dbcluster_serverless(
        self,
        request: polardb_20170801_models.EnableDBClusterServerlessRequest,
    ) -> polardb_20170801_models.EnableDBClusterServerlessResponse:
        """
        @summary Enables a stable serverless cluster.
        
        @param request: EnableDBClusterServerlessRequest
        @return: EnableDBClusterServerlessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_dbcluster_serverless_with_options(request, runtime)

    async def enable_dbcluster_serverless_async(
        self,
        request: polardb_20170801_models.EnableDBClusterServerlessRequest,
    ) -> polardb_20170801_models.EnableDBClusterServerlessResponse:
        """
        @summary Enables a stable serverless cluster.
        
        @param request: EnableDBClusterServerlessRequest
        @return: EnableDBClusterServerlessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_dbcluster_serverless_with_options_async(request, runtime)

    def enable_firewall_rules_with_options(
        self,
        request: polardb_20170801_models.EnableFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.EnableFirewallRulesResponse:
        """
        @summary 修改sql防火墙状态
        
        @param request: EnableFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableFirewallRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFirewallRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.EnableFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_firewall_rules_with_options_async(
        self,
        request: polardb_20170801_models.EnableFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.EnableFirewallRulesResponse:
        """
        @summary 修改sql防火墙状态
        
        @param request: EnableFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableFirewallRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFirewallRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.EnableFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_firewall_rules(
        self,
        request: polardb_20170801_models.EnableFirewallRulesRequest,
    ) -> polardb_20170801_models.EnableFirewallRulesResponse:
        """
        @summary 修改sql防火墙状态
        
        @param request: EnableFirewallRulesRequest
        @return: EnableFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_firewall_rules_with_options(request, runtime)

    async def enable_firewall_rules_async(
        self,
        request: polardb_20170801_models.EnableFirewallRulesRequest,
    ) -> polardb_20170801_models.EnableFirewallRulesResponse:
        """
        @summary 修改sql防火墙状态
        
        @param request: EnableFirewallRulesRequest
        @return: EnableFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_firewall_rules_with_options_async(request, runtime)

    def evaluate_region_resource_with_options(
        self,
        request: polardb_20170801_models.EvaluateRegionResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.EvaluateRegionResourceResponse:
        """
        @summary Evaluates available resources.
        
        @param request: EvaluateRegionResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluateRegionResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_conn_type):
            query['DBInstanceConnType'] = request.dbinstance_conn_type
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.dispense_mode):
            query['DispenseMode'] = request.dispense_mode
        if not UtilClient.is_unset(request.need_max_scale_link):
            query['NeedMaxScaleLink'] = request.need_max_scale_link
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EvaluateRegionResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.EvaluateRegionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_region_resource_with_options_async(
        self,
        request: polardb_20170801_models.EvaluateRegionResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.EvaluateRegionResourceResponse:
        """
        @summary Evaluates available resources.
        
        @param request: EvaluateRegionResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EvaluateRegionResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_conn_type):
            query['DBInstanceConnType'] = request.dbinstance_conn_type
        if not UtilClient.is_unset(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not UtilClient.is_unset(request.dbtype):
            query['DBType'] = request.dbtype
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.dispense_mode):
            query['DispenseMode'] = request.dispense_mode
        if not UtilClient.is_unset(request.need_max_scale_link):
            query['NeedMaxScaleLink'] = request.need_max_scale_link
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_domain):
            query['SubDomain'] = request.sub_domain
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EvaluateRegionResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.EvaluateRegionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_region_resource(
        self,
        request: polardb_20170801_models.EvaluateRegionResourceRequest,
    ) -> polardb_20170801_models.EvaluateRegionResourceResponse:
        """
        @summary Evaluates available resources.
        
        @param request: EvaluateRegionResourceRequest
        @return: EvaluateRegionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.evaluate_region_resource_with_options(request, runtime)

    async def evaluate_region_resource_async(
        self,
        request: polardb_20170801_models.EvaluateRegionResourceRequest,
    ) -> polardb_20170801_models.EvaluateRegionResourceResponse:
        """
        @summary Evaluates available resources.
        
        @param request: EvaluateRegionResourceRequest
        @return: EvaluateRegionResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_region_resource_with_options_async(request, runtime)

    def failover_dbcluster_with_options(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        """
        @summary Performs a manual failover to promote a read-only node to the primary node in a PolarDB cluster.
        
        @param request: FailoverDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailoverDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.roll_back_for_disaster):
            query['RollBackForDisaster'] = request.roll_back_for_disaster
        if not UtilClient.is_unset(request.target_dbnode_id):
            query['TargetDBNodeId'] = request.target_dbnode_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.FailoverDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        """
        @summary Performs a manual failover to promote a read-only node to the primary node in a PolarDB cluster.
        
        @param request: FailoverDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailoverDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if not UtilClient.is_unset(request.roll_back_for_disaster):
            query['RollBackForDisaster'] = request.roll_back_for_disaster
        if not UtilClient.is_unset(request.target_dbnode_id):
            query['TargetDBNodeId'] = request.target_dbnode_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.FailoverDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_dbcluster(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        """
        @summary Performs a manual failover to promote a read-only node to the primary node in a PolarDB cluster.
        
        @param request: FailoverDBClusterRequest
        @return: FailoverDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.failover_dbcluster_with_options(request, runtime)

    async def failover_dbcluster_async(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        """
        @summary Performs a manual failover to promote a read-only node to the primary node in a PolarDB cluster.
        
        @param request: FailoverDBClusterRequest
        @return: FailoverDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.failover_dbcluster_with_options_async(request, runtime)

    def grant_account_privilege_with_options(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        """
        @summary Grants a standard account the permissions to access one or more databases in a specified PolarDB cluster.
        
        @description >    An account can be authorized to access one or more databases.
        >    If the specified account already has the access permissions on the specified databases, the operation returns a successful response.
        >    Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        >    You can call this operation only on a PolarDB for MySQL cluster.
        >    By default, a privileged account for a cluster has all the permissions on the databases in the cluster.
        
        @param request: GrantAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='GrantAccountPrivilege',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.GrantAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_account_privilege_with_options_async(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        """
        @summary Grants a standard account the permissions to access one or more databases in a specified PolarDB cluster.
        
        @description >    An account can be authorized to access one or more databases.
        >    If the specified account already has the access permissions on the specified databases, the operation returns a successful response.
        >    Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        >    You can call this operation only on a PolarDB for MySQL cluster.
        >    By default, a privileged account for a cluster has all the permissions on the databases in the cluster.
        
        @param request: GrantAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='GrantAccountPrivilege',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.GrantAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_account_privilege(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        """
        @summary Grants a standard account the permissions to access one or more databases in a specified PolarDB cluster.
        
        @description >    An account can be authorized to access one or more databases.
        >    If the specified account already has the access permissions on the specified databases, the operation returns a successful response.
        >    Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        >    You can call this operation only on a PolarDB for MySQL cluster.
        >    By default, a privileged account for a cluster has all the permissions on the databases in the cluster.
        
        @param request: GrantAccountPrivilegeRequest
        @return: GrantAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    async def grant_account_privilege_async(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        """
        @summary Grants a standard account the permissions to access one or more databases in a specified PolarDB cluster.
        
        @description >    An account can be authorized to access one or more databases.
        >    If the specified account already has the access permissions on the specified databases, the operation returns a successful response.
        >    Before you call this operation, make sure that the cluster is in the Running state. Otherwise, the operation fails.
        >    You can call this operation only on a PolarDB for MySQL cluster.
        >    By default, a privileged account for a cluster has all the permissions on the databases in the cluster.
        
        @param request: GrantAccountPrivilegeRequest
        @return: GrantAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_account_privilege_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more PolarDB clusters, or queries the PolarDB clusters to which one or more tags are bound.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more PolarDB clusters, or queries the PolarDB clusters to which one or more tags are bound.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more PolarDB clusters, or queries the PolarDB clusters to which one or more tags are bound.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more PolarDB clusters, or queries the PolarDB clusters to which one or more tags are bound.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def manually_start_dbcluster_with_options(
        self,
        request: polardb_20170801_models.ManuallyStartDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ManuallyStartDBClusterResponse:
        """
        @summary Manually starts a cluster.
        
        @param request: ManuallyStartDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManuallyStartDBClusterResponse
        """
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
            action='ManuallyStartDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ManuallyStartDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def manually_start_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.ManuallyStartDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ManuallyStartDBClusterResponse:
        """
        @summary Manually starts a cluster.
        
        @param request: ManuallyStartDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManuallyStartDBClusterResponse
        """
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
            action='ManuallyStartDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ManuallyStartDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manually_start_dbcluster(
        self,
        request: polardb_20170801_models.ManuallyStartDBClusterRequest,
    ) -> polardb_20170801_models.ManuallyStartDBClusterResponse:
        """
        @summary Manually starts a cluster.
        
        @param request: ManuallyStartDBClusterRequest
        @return: ManuallyStartDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manually_start_dbcluster_with_options(request, runtime)

    async def manually_start_dbcluster_async(
        self,
        request: polardb_20170801_models.ManuallyStartDBClusterRequest,
    ) -> polardb_20170801_models.ManuallyStartDBClusterResponse:
        """
        @summary Manually starts a cluster.
        
        @param request: ManuallyStartDBClusterRequest
        @return: ManuallyStartDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manually_start_dbcluster_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of a PolarDB cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
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
            action='ModifyAccountDescription',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of a PolarDB cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
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
            action='ModifyAccountDescription',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of a PolarDB cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account of a PolarDB cluster.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_password_with_options(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a database account for a specified PolarDB cluster.
        
        @param request: ModifyAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_type):
            query['PasswordType'] = request.password_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPassword',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_password_with_options_async(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a database account for a specified PolarDB cluster.
        
        @param request: ModifyAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_type):
            query['PasswordType'] = request.password_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountPassword',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_password(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a database account for a specified PolarDB cluster.
        
        @param request: ModifyAccountPasswordRequest
        @return: ModifyAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    async def modify_account_password_async(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        """
        @summary Changes the password of a database account for a specified PolarDB cluster.
        
        @param request: ModifyAccountPasswordRequest
        @return: ModifyAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_password_with_options_async(request, runtime)

    def modify_auto_renew_attribute_with_options(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoRenewAttribute',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_renew_attribute_with_options_async(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoRenewAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoRenewAttribute',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_renew_attribute(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @return: ModifyAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_renew_attribute_with_options(request, runtime)

    async def modify_auto_renew_attribute_async(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        """
        @summary Modifies the auto-renewal attributes of a subscription PolarDB cluster.
        
        @param request: ModifyAutoRenewAttributeRequest
        @return: ModifyAutoRenewAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_renew_attribute_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of a PolarDB cluster.
        
        @description > You can also modify the automatic backup policy of a PolarDB cluster in the console. For more information, see [Backup settings](https://help.aliyun.com/document_detail/280422.html).
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_frequency):
            query['BackupFrequency'] = request.backup_frequency
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data_level_1backup_frequency):
            query['DataLevel1BackupFrequency'] = request.data_level_1backup_frequency
        if not UtilClient.is_unset(request.data_level_1backup_period):
            query['DataLevel1BackupPeriod'] = request.data_level_1backup_period
        if not UtilClient.is_unset(request.data_level_1backup_retention_period):
            query['DataLevel1BackupRetentionPeriod'] = request.data_level_1backup_retention_period
        if not UtilClient.is_unset(request.data_level_1backup_time):
            query['DataLevel1BackupTime'] = request.data_level_1backup_time
        if not UtilClient.is_unset(request.data_level_2backup_another_region_region):
            query['DataLevel2BackupAnotherRegionRegion'] = request.data_level_2backup_another_region_region
        if not UtilClient.is_unset(request.data_level_2backup_another_region_retention_period):
            query['DataLevel2BackupAnotherRegionRetentionPeriod'] = request.data_level_2backup_another_region_retention_period
        if not UtilClient.is_unset(request.data_level_2backup_period):
            query['DataLevel2BackupPeriod'] = request.data_level_2backup_period
        if not UtilClient.is_unset(request.data_level_2backup_retention_period):
            query['DataLevel2BackupRetentionPeriod'] = request.data_level_2backup_retention_period
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of a PolarDB cluster.
        
        @description > You can also modify the automatic backup policy of a PolarDB cluster in the console. For more information, see [Backup settings](https://help.aliyun.com/document_detail/280422.html).
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_frequency):
            query['BackupFrequency'] = request.backup_frequency
        if not UtilClient.is_unset(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data_level_1backup_frequency):
            query['DataLevel1BackupFrequency'] = request.data_level_1backup_frequency
        if not UtilClient.is_unset(request.data_level_1backup_period):
            query['DataLevel1BackupPeriod'] = request.data_level_1backup_period
        if not UtilClient.is_unset(request.data_level_1backup_retention_period):
            query['DataLevel1BackupRetentionPeriod'] = request.data_level_1backup_retention_period
        if not UtilClient.is_unset(request.data_level_1backup_time):
            query['DataLevel1BackupTime'] = request.data_level_1backup_time
        if not UtilClient.is_unset(request.data_level_2backup_another_region_region):
            query['DataLevel2BackupAnotherRegionRegion'] = request.data_level_2backup_another_region_region
        if not UtilClient.is_unset(request.data_level_2backup_another_region_retention_period):
            query['DataLevel2BackupAnotherRegionRetentionPeriod'] = request.data_level_2backup_another_region_retention_period
        if not UtilClient.is_unset(request.data_level_2backup_period):
            query['DataLevel2BackupPeriod'] = request.data_level_2backup_period
        if not UtilClient.is_unset(request.data_level_2backup_retention_period):
            query['DataLevel2BackupRetentionPeriod'] = request.data_level_2backup_retention_period
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
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of a PolarDB cluster.
        
        @description > You can also modify the automatic backup policy of a PolarDB cluster in the console. For more information, see [Backup settings](https://help.aliyun.com/document_detail/280422.html).
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        """
        @summary Modifies the automatic backup policy of a PolarDB cluster.
        
        @description > You can also modify the automatic backup policy of a PolarDB cluster in the console. For more information, see [Backup settings](https://help.aliyun.com/document_detail/280422.html).
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterResponse:
        """
        @summary Modifies the configurations of a PolarDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compress_storage):
            query['CompressStorage'] = request.compress_storage
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_crash_list):
            query['DBNodeCrashList'] = request.dbnode_crash_list
        if not UtilClient.is_unset(request.data_sync_mode):
            query['DataSyncMode'] = request.data_sync_mode
        if not UtilClient.is_unset(request.fault_injection_type):
            query['FaultInjectionType'] = request.fault_injection_type
        if not UtilClient.is_unset(request.fault_simulate_mode):
            query['FaultSimulateMode'] = request.fault_simulate_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.standby_hamode):
            query['StandbyHAMode'] = request.standby_hamode
        if not UtilClient.is_unset(request.storage_auto_scale):
            query['StorageAutoScale'] = request.storage_auto_scale
        if not UtilClient.is_unset(request.storage_upper_bound):
            query['StorageUpperBound'] = request.storage_upper_bound
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterResponse:
        """
        @summary Modifies the configurations of a PolarDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compress_storage):
            query['CompressStorage'] = request.compress_storage
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_crash_list):
            query['DBNodeCrashList'] = request.dbnode_crash_list
        if not UtilClient.is_unset(request.data_sync_mode):
            query['DataSyncMode'] = request.data_sync_mode
        if not UtilClient.is_unset(request.fault_injection_type):
            query['FaultInjectionType'] = request.fault_injection_type
        if not UtilClient.is_unset(request.fault_simulate_mode):
            query['FaultSimulateMode'] = request.fault_simulate_mode
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.standby_hamode):
            query['StandbyHAMode'] = request.standby_hamode
        if not UtilClient.is_unset(request.storage_auto_scale):
            query['StorageAutoScale'] = request.storage_auto_scale
        if not UtilClient.is_unset(request.storage_upper_bound):
            query['StorageUpperBound'] = request.storage_upper_bound
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: polardb_20170801_models.ModifyDBClusterRequest,
    ) -> polardb_20170801_models.ModifyDBClusterResponse:
        """
        @summary Modifies the configurations of a PolarDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterRequest,
    ) -> polardb_20170801_models.ModifyDBClusterResponse:
        """
        @summary Modifies the configurations of a PolarDB for MySQL cluster.
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_access_whitelist_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        """
        @summary Creates or modifies the whitelists (IP whitelists and security groups) of a specified cluster.
        
        @param request: ModifyDBClusterAccessWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAccessWhitelistResponse
        """
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhitelist',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_access_whitelist_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        """
        @summary Creates or modifies the whitelists (IP whitelists and security groups) of a specified cluster.
        
        @param request: ModifyDBClusterAccessWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAccessWhitelistResponse
        """
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhitelist',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_access_whitelist(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        """
        @summary Creates or modifies the whitelists (IP whitelists and security groups) of a specified cluster.
        
        @param request: ModifyDBClusterAccessWhitelistRequest
        @return: ModifyDBClusterAccessWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_whitelist_with_options(request, runtime)

    async def modify_dbcluster_access_whitelist_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        """
        @summary Creates or modifies the whitelists (IP whitelists and security groups) of a specified cluster.
        
        @param request: ModifyDBClusterAccessWhitelistRequest
        @return: ModifyDBClusterAccessWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_access_whitelist_with_options_async(request, runtime)

    def modify_dbcluster_and_nodes_parameters_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterAndNodesParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAndNodesParametersResponse:
        """
        @summary Modifies cluster parameters and applies them to specified nodes.
        
        @param request: ModifyDBClusterAndNodesParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAndNodesParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAndNodesParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterAndNodesParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_and_nodes_parameters_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAndNodesParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAndNodesParametersResponse:
        """
        @summary Modifies cluster parameters and applies them to specified nodes.
        
        @param request: ModifyDBClusterAndNodesParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAndNodesParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAndNodesParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterAndNodesParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_and_nodes_parameters(
        self,
        request: polardb_20170801_models.ModifyDBClusterAndNodesParametersRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAndNodesParametersResponse:
        """
        @summary Modifies cluster parameters and applies them to specified nodes.
        
        @param request: ModifyDBClusterAndNodesParametersRequest
        @return: ModifyDBClusterAndNodesParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_and_nodes_parameters_with_options(request, runtime)

    async def modify_dbcluster_and_nodes_parameters_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAndNodesParametersRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAndNodesParametersResponse:
        """
        @summary Modifies cluster parameters and applies them to specified nodes.
        
        @param request: ModifyDBClusterAndNodesParametersRequest
        @return: ModifyDBClusterAndNodesParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_and_nodes_parameters_with_options_async(request, runtime)

    def modify_dbcluster_audit_log_collector_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        """
        @summary Enables or disables SQL collector for a PolarDB cluster. The features related to SQL collector include Audit Logs and SQL Explorer.
        
        @param request: ModifyDBClusterAuditLogCollectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAuditLogCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collector_status):
            query['CollectorStatus'] = request.collector_status
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
            action='ModifyDBClusterAuditLogCollector',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_audit_log_collector_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        """
        @summary Enables or disables SQL collector for a PolarDB cluster. The features related to SQL collector include Audit Logs and SQL Explorer.
        
        @param request: ModifyDBClusterAuditLogCollectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterAuditLogCollectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collector_status):
            query['CollectorStatus'] = request.collector_status
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
            action='ModifyDBClusterAuditLogCollector',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_audit_log_collector(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        """
        @summary Enables or disables SQL collector for a PolarDB cluster. The features related to SQL collector include Audit Logs and SQL Explorer.
        
        @param request: ModifyDBClusterAuditLogCollectorRequest
        @return: ModifyDBClusterAuditLogCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_audit_log_collector_with_options(request, runtime)

    async def modify_dbcluster_audit_log_collector_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        """
        @summary Enables or disables SQL collector for a PolarDB cluster. The features related to SQL collector include Audit Logs and SQL Explorer.
        
        @param request: ModifyDBClusterAuditLogCollectorRequest
        @return: ModifyDBClusterAuditLogCollectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_audit_log_collector_with_options_async(request, runtime)

    def modify_dbcluster_deletion_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterDeletionResponse:
        """
        @summary Enables or disables the cluster lock feature for a PolarDB cluster.
        
        @param request: ModifyDBClusterDeletionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDeletionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection):
            query['Protection'] = request.protection
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDeletion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterDeletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_deletion_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterDeletionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterDeletionResponse:
        """
        @summary Enables or disables the cluster lock feature for a PolarDB cluster.
        
        @param request: ModifyDBClusterDeletionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDeletionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protection):
            query['Protection'] = request.protection
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDeletion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterDeletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_deletion(
        self,
        request: polardb_20170801_models.ModifyDBClusterDeletionRequest,
    ) -> polardb_20170801_models.ModifyDBClusterDeletionResponse:
        """
        @summary Enables or disables the cluster lock feature for a PolarDB cluster.
        
        @param request: ModifyDBClusterDeletionRequest
        @return: ModifyDBClusterDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_deletion_with_options(request, runtime)

    async def modify_dbcluster_deletion_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterDeletionRequest,
    ) -> polardb_20170801_models.ModifyDBClusterDeletionResponse:
        """
        @summary Enables or disables the cluster lock feature for a PolarDB cluster.
        
        @param request: ModifyDBClusterDeletionRequest
        @return: ModifyDBClusterDeletionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_deletion_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the name of a PolarDB cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
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
            action='ModifyDBClusterDescription',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the name of a PolarDB cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
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
            action='ModifyDBClusterDescription',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the name of a PolarDB cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        """
        @summary Modifies the name of a PolarDB cluster.
        
        @param request: ModifyDBClusterDescriptionRequest
        @return: ModifyDBClusterDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_endpoint_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        """
        @summary Modifies the attributes of a specified PolarDB cluster endpoint. For example, you can modify the following attributes for the specified cluster endpoint: read/write mode, consistency level, transaction splitting, primary node accepts read requests, and connection pool. You can also call the operation to specify whether newly added nodes are automatically associated with the specified cluster endpoint.
        
        @param request: ModifyDBClusterEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_add_new_nodes):
            query['AutoAddNewNodes'] = request.auto_add_new_nodes
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_description):
            query['DBEndpointDescription'] = request.dbendpoint_description
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.endpoint_config):
            query['EndpointConfig'] = request.endpoint_config
        if not UtilClient.is_unset(request.nodes):
            query['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.polar_scc_timeout_action):
            query['PolarSccTimeoutAction'] = request.polar_scc_timeout_action
        if not UtilClient.is_unset(request.polar_scc_wait_timeout):
            query['PolarSccWaitTimeout'] = request.polar_scc_wait_timeout
        if not UtilClient.is_unset(request.read_write_mode):
            query['ReadWriteMode'] = request.read_write_mode
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scc_mode):
            query['SccMode'] = request.scc_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterEndpoint',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_endpoint_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        """
        @summary Modifies the attributes of a specified PolarDB cluster endpoint. For example, you can modify the following attributes for the specified cluster endpoint: read/write mode, consistency level, transaction splitting, primary node accepts read requests, and connection pool. You can also call the operation to specify whether newly added nodes are automatically associated with the specified cluster endpoint.
        
        @param request: ModifyDBClusterEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_add_new_nodes):
            query['AutoAddNewNodes'] = request.auto_add_new_nodes
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_description):
            query['DBEndpointDescription'] = request.dbendpoint_description
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.endpoint_config):
            query['EndpointConfig'] = request.endpoint_config
        if not UtilClient.is_unset(request.nodes):
            query['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.polar_scc_timeout_action):
            query['PolarSccTimeoutAction'] = request.polar_scc_timeout_action
        if not UtilClient.is_unset(request.polar_scc_wait_timeout):
            query['PolarSccWaitTimeout'] = request.polar_scc_wait_timeout
        if not UtilClient.is_unset(request.read_write_mode):
            query['ReadWriteMode'] = request.read_write_mode
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scc_mode):
            query['SccMode'] = request.scc_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterEndpoint',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_endpoint(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        """
        @summary Modifies the attributes of a specified PolarDB cluster endpoint. For example, you can modify the following attributes for the specified cluster endpoint: read/write mode, consistency level, transaction splitting, primary node accepts read requests, and connection pool. You can also call the operation to specify whether newly added nodes are automatically associated with the specified cluster endpoint.
        
        @param request: ModifyDBClusterEndpointRequest
        @return: ModifyDBClusterEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_endpoint_with_options(request, runtime)

    async def modify_dbcluster_endpoint_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        """
        @summary Modifies the attributes of a specified PolarDB cluster endpoint. For example, you can modify the following attributes for the specified cluster endpoint: read/write mode, consistency level, transaction splitting, primary node accepts read requests, and connection pool. You can also call the operation to specify whether newly added nodes are automatically associated with the specified cluster endpoint.
        
        @param request: ModifyDBClusterEndpointRequest
        @return: ModifyDBClusterEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_endpoint_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of a PolarDB cluster.
        
        @description >  We recommend that you set the routine maintenance window to off-peak hours. Alibaba Cloud maintains your cluster within the specified maintenance window to minimize the negative impacts on your business.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
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
            action='ModifyDBClusterMaintainTime',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of a PolarDB cluster.
        
        @description >  We recommend that you set the routine maintenance window to off-peak hours. Alibaba Cloud maintains your cluster within the specified maintenance window to minimize the negative impacts on your business.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
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
            action='ModifyDBClusterMaintainTime',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of a PolarDB cluster.
        
        @description >  We recommend that you set the routine maintenance window to off-peak hours. Alibaba Cloud maintains your cluster within the specified maintenance window to minimize the negative impacts on your business.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        """
        @summary Modifies the maintenance window of a PolarDB cluster.
        
        @description >  We recommend that you set the routine maintenance window to off-peak hours. Alibaba Cloud maintains your cluster within the specified maintenance window to minimize the negative impacts on your business.
        
        @param request: ModifyDBClusterMaintainTimeRequest
        @return: ModifyDBClusterMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbcluster_migration_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        """
        @summary Switches or rolls back the task that migrates data from ApsaraDB for RDS to PolarDB.
        
        @description    You can call this operation to switch the task that migrates data from ApsaraDB for RDS to PolarDB.
        You can call this operation to roll back the task that migrates data from ApsaraDB for RDS to PolarDB.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: ModifyDBClusterMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_strings):
            query['ConnectionStrings'] = request.connection_strings
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_master_instance_id):
            query['NewMasterInstanceId'] = request.new_master_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_rdsdbinstance_id):
            query['SourceRDSDBInstanceId'] = request.source_rdsdbinstance_id
        if not UtilClient.is_unset(request.swap_connection_string):
            query['SwapConnectionString'] = request.swap_connection_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMigration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_migration_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        """
        @summary Switches or rolls back the task that migrates data from ApsaraDB for RDS to PolarDB.
        
        @description    You can call this operation to switch the task that migrates data from ApsaraDB for RDS to PolarDB.
        You can call this operation to roll back the task that migrates data from ApsaraDB for RDS to PolarDB.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: ModifyDBClusterMigrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMigrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_strings):
            query['ConnectionStrings'] = request.connection_strings
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_master_instance_id):
            query['NewMasterInstanceId'] = request.new_master_instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_rdsdbinstance_id):
            query['SourceRDSDBInstanceId'] = request.source_rdsdbinstance_id
        if not UtilClient.is_unset(request.swap_connection_string):
            query['SwapConnectionString'] = request.swap_connection_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMigration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_migration(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        """
        @summary Switches or rolls back the task that migrates data from ApsaraDB for RDS to PolarDB.
        
        @description    You can call this operation to switch the task that migrates data from ApsaraDB for RDS to PolarDB.
        You can call this operation to roll back the task that migrates data from ApsaraDB for RDS to PolarDB.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: ModifyDBClusterMigrationRequest
        @return: ModifyDBClusterMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_migration_with_options(request, runtime)

    async def modify_dbcluster_migration_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        """
        @summary Switches or rolls back the task that migrates data from ApsaraDB for RDS to PolarDB.
        
        @description    You can call this operation to switch the task that migrates data from ApsaraDB for RDS to PolarDB.
        You can call this operation to roll back the task that migrates data from ApsaraDB for RDS to PolarDB.
        > Before you call this operation, ensure that a one-click upgrade task has been created for the cluster. You can call the [CreateDBCluster](https://help.aliyun.com/document_detail/98169.html) operation to create an upgrade task. Set the *CreationOption** parameter to **MigrationFromRDS**. For more information, see [Create a PolarDB for MySQL cluster by using the Migration from RDS method](https://help.aliyun.com/document_detail/121582.html).
        
        @param request: ModifyDBClusterMigrationRequest
        @return: ModifyDBClusterMigrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_migration_with_options_async(request, runtime)

    def modify_dbcluster_monitor_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        """
        @summary Modifies the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        
        @param request: ModifyDBClusterMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMonitor',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_monitor_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        """
        @summary Modifies the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        
        @param request: ModifyDBClusterMonitorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterMonitorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMonitor',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_monitor(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        """
        @summary Modifies the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        
        @param request: ModifyDBClusterMonitorRequest
        @return: ModifyDBClusterMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_monitor_with_options(request, runtime)

    async def modify_dbcluster_monitor_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        """
        @summary Modifies the interval at which the monitoring data of a PolarDB cluster is collected.
        
        @description    When the monitoring data is collected every 5 seconds:
        If the query time range is less than or equal to 1 hour, the data is displayed at intervals of 5 seconds.
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        When the monitoring data is collected every 60 seconds:
        If the query time range is less than or equal to one day, the data is displayed at intervals of 1 minute.
        If the query time range is less than or equal to seven days, the data is displayed at intervals of 10 minutes.
        If the query time range is less than or equal to 30 days, the data is displayed at intervals of 1 hour.
        When the query time range is greater than 30 days, the data is displayed at intervals of 1 day.
        
        @param request: ModifyDBClusterMonitorRequest
        @return: ModifyDBClusterMonitorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_monitor_with_options_async(request, runtime)

    def modify_dbcluster_parameters_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        """
        @summary Modifies the parameters of a specified PolarDB cluster or applies existing parameter templates to a specified cluster.
        
        @description PolarDB supports the parameter template feature to centrally manage clusters. You can configure a number of parameters at a time by using a parameter template and apply the template to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        *\
        *Only PolarDB for MySQL clusters support parameter templates.
        
        @param request: ModifyDBClusterParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_parameters_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        """
        @summary Modifies the parameters of a specified PolarDB cluster or applies existing parameter templates to a specified cluster.
        
        @description PolarDB supports the parameter template feature to centrally manage clusters. You can configure a number of parameters at a time by using a parameter template and apply the template to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        *\
        *Only PolarDB for MySQL clusters support parameter templates.
        
        @param request: ModifyDBClusterParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_parameters(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        """
        @summary Modifies the parameters of a specified PolarDB cluster or applies existing parameter templates to a specified cluster.
        
        @description PolarDB supports the parameter template feature to centrally manage clusters. You can configure a number of parameters at a time by using a parameter template and apply the template to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        *\
        *Only PolarDB for MySQL clusters support parameter templates.
        
        @param request: ModifyDBClusterParametersRequest
        @return: ModifyDBClusterParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_parameters_with_options(request, runtime)

    async def modify_dbcluster_parameters_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        """
        @summary Modifies the parameters of a specified PolarDB cluster or applies existing parameter templates to a specified cluster.
        
        @description PolarDB supports the parameter template feature to centrally manage clusters. You can configure a number of parameters at a time by using a parameter template and apply the template to a PolarDB cluster. For more information, see [Use a parameter template](https://help.aliyun.com/document_detail/207009.html).
        *\
        *Only PolarDB for MySQL clusters support parameter templates.
        
        @param request: ModifyDBClusterParametersRequest
        @return: ModifyDBClusterParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_parameters_with_options_async(request, runtime)

    def modify_dbcluster_primary_zone_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        """
        @summary Changes the primary zone of a PolarDB cluster.
        
        @param request: ModifyDBClusterPrimaryZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterPrimaryZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.is_switch_over_for_disaster):
            query['IsSwitchOverForDisaster'] = request.is_switch_over_for_disaster
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterPrimaryZone',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_primary_zone_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        """
        @summary Changes the primary zone of a PolarDB cluster.
        
        @param request: ModifyDBClusterPrimaryZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterPrimaryZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.is_switch_over_for_disaster):
            query['IsSwitchOverForDisaster'] = request.is_switch_over_for_disaster
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterPrimaryZone',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_primary_zone(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        """
        @summary Changes the primary zone of a PolarDB cluster.
        
        @param request: ModifyDBClusterPrimaryZoneRequest
        @return: ModifyDBClusterPrimaryZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_primary_zone_with_options(request, runtime)

    async def modify_dbcluster_primary_zone_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        """
        @summary Changes the primary zone of a PolarDB cluster.
        
        @param request: ModifyDBClusterPrimaryZoneRequest
        @return: ModifyDBClusterPrimaryZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_primary_zone_with_options_async(request, runtime)

    def modify_dbcluster_resource_group_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterResourceGroupResponse:
        """
        @param request: ModifyDBClusterResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterResourceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_resource_group_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterResourceGroupResponse:
        """
        @param request: ModifyDBClusterResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterResourceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_resource_group(
        self,
        request: polardb_20170801_models.ModifyDBClusterResourceGroupRequest,
    ) -> polardb_20170801_models.ModifyDBClusterResourceGroupResponse:
        """
        @param request: ModifyDBClusterResourceGroupRequest
        @return: ModifyDBClusterResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_resource_group_with_options(request, runtime)

    async def modify_dbcluster_resource_group_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterResourceGroupRequest,
    ) -> polardb_20170801_models.ModifyDBClusterResourceGroupResponse:
        """
        @param request: ModifyDBClusterResourceGroupRequest
        @return: ModifyDBClusterResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_resource_group_with_options_async(request, runtime)

    def modify_dbcluster_sslwith_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        """
        @summary Enables or disables Secure Sockets Layer (SSL) encryption or updates the Certificate Authorities (CA) certificate for a specified PolarDB cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslauto_rotate):
            query['SSLAutoRotate'] = request.sslauto_rotate
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterSSL',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_sslwith_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        """
        @summary Enables or disables Secure Sockets Layer (SSL) encryption or updates the Certificate Authorities (CA) certificate for a specified PolarDB cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sslauto_rotate):
            query['SSLAutoRotate'] = request.sslauto_rotate
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterSSL',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_ssl(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        """
        @summary Enables or disables Secure Sockets Layer (SSL) encryption or updates the Certificate Authorities (CA) certificate for a specified PolarDB cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @return: ModifyDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_sslwith_options(request, runtime)

    async def modify_dbcluster_ssl_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        """
        @summary Enables or disables Secure Sockets Layer (SSL) encryption or updates the Certificate Authorities (CA) certificate for a specified PolarDB cluster.
        
        @param request: ModifyDBClusterSSLRequest
        @return: ModifyDBClusterSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_sslwith_options_async(request, runtime)

    def modify_dbcluster_serverless_conf_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterServerlessConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterServerlessConfResponse:
        """
        @summary Modifies the configurations of a serverless cluster.
        
        @param request: ModifyDBClusterServerlessConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterServerlessConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_shut_down):
            query['AllowShutDown'] = request.allow_shut_down
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_ap_ro_num_max):
            query['ScaleApRoNumMax'] = request.scale_ap_ro_num_max
        if not UtilClient.is_unset(request.scale_ap_ro_num_min):
            query['ScaleApRoNumMin'] = request.scale_ap_ro_num_min
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.scale_ro_num_max):
            query['ScaleRoNumMax'] = request.scale_ro_num_max
        if not UtilClient.is_unset(request.scale_ro_num_min):
            query['ScaleRoNumMin'] = request.scale_ro_num_min
        if not UtilClient.is_unset(request.seconds_until_auto_pause):
            query['SecondsUntilAutoPause'] = request.seconds_until_auto_pause
        if not UtilClient.is_unset(request.serverless_rule_cpu_enlarge_threshold):
            query['ServerlessRuleCpuEnlargeThreshold'] = request.serverless_rule_cpu_enlarge_threshold
        if not UtilClient.is_unset(request.serverless_rule_cpu_shrink_threshold):
            query['ServerlessRuleCpuShrinkThreshold'] = request.serverless_rule_cpu_shrink_threshold
        if not UtilClient.is_unset(request.serverless_rule_mode):
            query['ServerlessRuleMode'] = request.serverless_rule_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterServerlessConf',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterServerlessConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_serverless_conf_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterServerlessConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterServerlessConfResponse:
        """
        @summary Modifies the configurations of a serverless cluster.
        
        @param request: ModifyDBClusterServerlessConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterServerlessConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_shut_down):
            query['AllowShutDown'] = request.allow_shut_down
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_ap_ro_num_max):
            query['ScaleApRoNumMax'] = request.scale_ap_ro_num_max
        if not UtilClient.is_unset(request.scale_ap_ro_num_min):
            query['ScaleApRoNumMin'] = request.scale_ap_ro_num_min
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.scale_ro_num_max):
            query['ScaleRoNumMax'] = request.scale_ro_num_max
        if not UtilClient.is_unset(request.scale_ro_num_min):
            query['ScaleRoNumMin'] = request.scale_ro_num_min
        if not UtilClient.is_unset(request.seconds_until_auto_pause):
            query['SecondsUntilAutoPause'] = request.seconds_until_auto_pause
        if not UtilClient.is_unset(request.serverless_rule_cpu_enlarge_threshold):
            query['ServerlessRuleCpuEnlargeThreshold'] = request.serverless_rule_cpu_enlarge_threshold
        if not UtilClient.is_unset(request.serverless_rule_cpu_shrink_threshold):
            query['ServerlessRuleCpuShrinkThreshold'] = request.serverless_rule_cpu_shrink_threshold
        if not UtilClient.is_unset(request.serverless_rule_mode):
            query['ServerlessRuleMode'] = request.serverless_rule_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterServerlessConf',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterServerlessConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_serverless_conf(
        self,
        request: polardb_20170801_models.ModifyDBClusterServerlessConfRequest,
    ) -> polardb_20170801_models.ModifyDBClusterServerlessConfResponse:
        """
        @summary Modifies the configurations of a serverless cluster.
        
        @param request: ModifyDBClusterServerlessConfRequest
        @return: ModifyDBClusterServerlessConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_serverless_conf_with_options(request, runtime)

    async def modify_dbcluster_serverless_conf_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterServerlessConfRequest,
    ) -> polardb_20170801_models.ModifyDBClusterServerlessConfResponse:
        """
        @summary Modifies the configurations of a serverless cluster.
        
        @param request: ModifyDBClusterServerlessConfRequest
        @return: ModifyDBClusterServerlessConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_serverless_conf_with_options_async(request, runtime)

    def modify_dbcluster_storage_space_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterStorageSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterStorageSpaceResponse:
        """
        @summary Changes the storage capacity of a pay-as-you-go cluster of Enterprise Edition or a cluster of Standard Edition.
        
        @param request: ModifyDBClusterStorageSpaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterStorageSpaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_space):
            query['StorageSpace'] = request.storage_space
        if not UtilClient.is_unset(request.sub_category):
            query['SubCategory'] = request.sub_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterStorageSpace',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterStorageSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_storage_space_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterStorageSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterStorageSpaceResponse:
        """
        @summary Changes the storage capacity of a pay-as-you-go cluster of Enterprise Edition or a cluster of Standard Edition.
        
        @param request: ModifyDBClusterStorageSpaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterStorageSpaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_space):
            query['StorageSpace'] = request.storage_space
        if not UtilClient.is_unset(request.sub_category):
            query['SubCategory'] = request.sub_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterStorageSpace',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterStorageSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_storage_space(
        self,
        request: polardb_20170801_models.ModifyDBClusterStorageSpaceRequest,
    ) -> polardb_20170801_models.ModifyDBClusterStorageSpaceResponse:
        """
        @summary Changes the storage capacity of a pay-as-you-go cluster of Enterprise Edition or a cluster of Standard Edition.
        
        @param request: ModifyDBClusterStorageSpaceRequest
        @return: ModifyDBClusterStorageSpaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_storage_space_with_options(request, runtime)

    async def modify_dbcluster_storage_space_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterStorageSpaceRequest,
    ) -> polardb_20170801_models.ModifyDBClusterStorageSpaceResponse:
        """
        @summary Changes the storage capacity of a pay-as-you-go cluster of Enterprise Edition or a cluster of Standard Edition.
        
        @param request: ModifyDBClusterStorageSpaceRequest
        @return: ModifyDBClusterStorageSpaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_storage_space_with_options_async(request, runtime)

    def modify_dbcluster_tdewith_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        """
        @summary Enables the TDE feature or changes the encryption method for a specified PolarDB for MySQL cluster.
        
        @description >    To perform this operation, you must activate KMS first. For more information, see [Purchase a dedicated KMS instance](https://help.aliyun.com/document_detail/153781.html).
        >    After TDE is enabled, you cannot disable TDE.
        
        @param request: ModifyDBClusterTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.encrypt_new_tables):
            query['EncryptNewTables'] = request.encrypt_new_tables
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterTDE',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_tdewith_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        """
        @summary Enables the TDE feature or changes the encryption method for a specified PolarDB for MySQL cluster.
        
        @description >    To perform this operation, you must activate KMS first. For more information, see [Purchase a dedicated KMS instance](https://help.aliyun.com/document_detail/153781.html).
        >    After TDE is enabled, you cannot disable TDE.
        
        @param request: ModifyDBClusterTDERequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterTDEResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.encrypt_new_tables):
            query['EncryptNewTables'] = request.encrypt_new_tables
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterTDE',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBClusterTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_tde(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        """
        @summary Enables the TDE feature or changes the encryption method for a specified PolarDB for MySQL cluster.
        
        @description >    To perform this operation, you must activate KMS first. For more information, see [Purchase a dedicated KMS instance](https://help.aliyun.com/document_detail/153781.html).
        >    After TDE is enabled, you cannot disable TDE.
        
        @param request: ModifyDBClusterTDERequest
        @return: ModifyDBClusterTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_tdewith_options(request, runtime)

    async def modify_dbcluster_tde_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        """
        @summary Enables the TDE feature or changes the encryption method for a specified PolarDB for MySQL cluster.
        
        @description >    To perform this operation, you must activate KMS first. For more information, see [Purchase a dedicated KMS instance](https://help.aliyun.com/document_detail/153781.html).
        >    After TDE is enabled, you cannot disable TDE.
        
        @param request: ModifyDBClusterTDERequest
        @return: ModifyDBClusterTDEResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_tdewith_options_async(request, runtime)

    def modify_dbdescription_with_options(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        """
        @summary Modifies the description of a database in a PolarDB for MySQL cluster.
        
        @param request: ModifyDBDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbdescription):
            query['DBDescription'] = request.dbdescription
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='ModifyDBDescription',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbdescription_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        """
        @summary Modifies the description of a database in a PolarDB for MySQL cluster.
        
        @param request: ModifyDBDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbdescription):
            query['DBDescription'] = request.dbdescription
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='ModifyDBDescription',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbdescription(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        """
        @summary Modifies the description of a database in a PolarDB for MySQL cluster.
        
        @param request: ModifyDBDescriptionRequest
        @return: ModifyDBDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    async def modify_dbdescription_async(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        """
        @summary Modifies the description of a database in a PolarDB for MySQL cluster.
        
        @param request: ModifyDBDescriptionRequest
        @return: ModifyDBDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbdescription_with_options_async(request, runtime)

    def modify_dbendpoint_address_with_options(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        """
        @summary Modifies the endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, custom cluster endpoint, and private domain name.
        
        @param request: ModifyDBEndpointAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_zone_address_prefix):
            query['PrivateZoneAddressPrefix'] = request.private_zone_address_prefix
        if not UtilClient.is_unset(request.private_zone_name):
            query['PrivateZoneName'] = request.private_zone_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBEndpointAddress',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBEndpointAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbendpoint_address_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        """
        @summary Modifies the endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, custom cluster endpoint, and private domain name.
        
        @param request: ModifyDBEndpointAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBEndpointAddressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbendpoint_id):
            query['DBEndpointId'] = request.dbendpoint_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_zone_address_prefix):
            query['PrivateZoneAddressPrefix'] = request.private_zone_address_prefix
        if not UtilClient.is_unset(request.private_zone_name):
            query['PrivateZoneName'] = request.private_zone_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBEndpointAddress',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBEndpointAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbendpoint_address(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        """
        @summary Modifies the endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, custom cluster endpoint, and private domain name.
        
        @param request: ModifyDBEndpointAddressRequest
        @return: ModifyDBEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbendpoint_address_with_options(request, runtime)

    async def modify_dbendpoint_address_async(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        """
        @summary Modifies the endpoints of a PolarDB cluster, including the primary endpoint, default cluster endpoint, custom cluster endpoint, and private domain name.
        
        @param request: ModifyDBEndpointAddressRequest
        @return: ModifyDBEndpointAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbendpoint_address_with_options_async(request, runtime)

    def modify_dbnode_class_with_options(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        """
        @summary Changes the node specifications of a PolarDB cluster.
        
        @param request: ModifyDBNodeClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodeClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_target_class):
            query['DBNodeTargetClass'] = request.dbnode_target_class
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_category):
            query['SubCategory'] = request.sub_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBNodeClass',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodeClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbnode_class_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        """
        @summary Changes the node specifications of a PolarDB cluster.
        
        @param request: ModifyDBNodeClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodeClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_target_class):
            query['DBNodeTargetClass'] = request.dbnode_target_class
        if not UtilClient.is_unset(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_category):
            query['SubCategory'] = request.sub_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBNodeClass',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodeClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbnode_class(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        """
        @summary Changes the node specifications of a PolarDB cluster.
        
        @param request: ModifyDBNodeClassRequest
        @return: ModifyDBNodeClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbnode_class_with_options(request, runtime)

    async def modify_dbnode_class_async(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        """
        @summary Changes the node specifications of a PolarDB cluster.
        
        @param request: ModifyDBNodeClassRequest
        @return: ModifyDBNodeClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbnode_class_with_options_async(request, runtime)

    def modify_dbnode_hot_replica_mode_with_options(
        self,
        request: polardb_20170801_models.ModifyDBNodeHotReplicaModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodeHotReplicaModeResponse:
        """
        @summary Enables or disables a cluster node.
        
        @param request: ModifyDBNodeHotReplicaModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodeHotReplicaModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
        if not UtilClient.is_unset(request.hot_replica_mode):
            query['HotReplicaMode'] = request.hot_replica_mode
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
            action='ModifyDBNodeHotReplicaMode',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodeHotReplicaModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbnode_hot_replica_mode_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBNodeHotReplicaModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodeHotReplicaModeResponse:
        """
        @summary Enables or disables a cluster node.
        
        @param request: ModifyDBNodeHotReplicaModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodeHotReplicaModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
        if not UtilClient.is_unset(request.hot_replica_mode):
            query['HotReplicaMode'] = request.hot_replica_mode
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
            action='ModifyDBNodeHotReplicaMode',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodeHotReplicaModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbnode_hot_replica_mode(
        self,
        request: polardb_20170801_models.ModifyDBNodeHotReplicaModeRequest,
    ) -> polardb_20170801_models.ModifyDBNodeHotReplicaModeResponse:
        """
        @summary Enables or disables a cluster node.
        
        @param request: ModifyDBNodeHotReplicaModeRequest
        @return: ModifyDBNodeHotReplicaModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbnode_hot_replica_mode_with_options(request, runtime)

    async def modify_dbnode_hot_replica_mode_async(
        self,
        request: polardb_20170801_models.ModifyDBNodeHotReplicaModeRequest,
    ) -> polardb_20170801_models.ModifyDBNodeHotReplicaModeResponse:
        """
        @summary Enables or disables a cluster node.
        
        @param request: ModifyDBNodeHotReplicaModeRequest
        @return: ModifyDBNodeHotReplicaModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbnode_hot_replica_mode_with_options_async(request, runtime)

    def modify_dbnodes_class_with_options(
        self,
        request: polardb_20170801_models.ModifyDBNodesClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodesClassResponse:
        """
        @summary Changes the specifications of a node in a PolarDB cluster.
        
        @param request: ModifyDBNodesClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodesClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode):
            query['DBNode'] = request.dbnode
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_category):
            query['SubCategory'] = request.sub_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBNodesClass',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodesClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbnodes_class_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBNodesClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodesClassResponse:
        """
        @summary Changes the specifications of a node in a PolarDB cluster.
        
        @param request: ModifyDBNodesClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodesClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode):
            query['DBNode'] = request.dbnode
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sub_category):
            query['SubCategory'] = request.sub_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBNodesClass',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodesClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbnodes_class(
        self,
        request: polardb_20170801_models.ModifyDBNodesClassRequest,
    ) -> polardb_20170801_models.ModifyDBNodesClassResponse:
        """
        @summary Changes the specifications of a node in a PolarDB cluster.
        
        @param request: ModifyDBNodesClassRequest
        @return: ModifyDBNodesClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbnodes_class_with_options(request, runtime)

    async def modify_dbnodes_class_async(
        self,
        request: polardb_20170801_models.ModifyDBNodesClassRequest,
    ) -> polardb_20170801_models.ModifyDBNodesClassResponse:
        """
        @summary Changes the specifications of a node in a PolarDB cluster.
        
        @param request: ModifyDBNodesClassRequest
        @return: ModifyDBNodesClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbnodes_class_with_options_async(request, runtime)

    def modify_dbnodes_parameters_with_options(
        self,
        request: polardb_20170801_models.ModifyDBNodesParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodesParametersResponse:
        """
        @summary Modifies the parameters of a node and applies them to specified nodes.
        
        @param request: ModifyDBNodesParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodesParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBNodesParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodesParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbnodes_parameters_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBNodesParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodesParametersResponse:
        """
        @summary Modifies the parameters of a node and applies them to specified nodes.
        
        @param request: ModifyDBNodesParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBNodesParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBNodesParameters',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyDBNodesParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbnodes_parameters(
        self,
        request: polardb_20170801_models.ModifyDBNodesParametersRequest,
    ) -> polardb_20170801_models.ModifyDBNodesParametersResponse:
        """
        @summary Modifies the parameters of a node and applies them to specified nodes.
        
        @param request: ModifyDBNodesParametersRequest
        @return: ModifyDBNodesParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbnodes_parameters_with_options(request, runtime)

    async def modify_dbnodes_parameters_async(
        self,
        request: polardb_20170801_models.ModifyDBNodesParametersRequest,
    ) -> polardb_20170801_models.ModifyDBNodesParametersResponse:
        """
        @summary Modifies the parameters of a node and applies them to specified nodes.
        
        @param request: ModifyDBNodesParametersRequest
        @return: ModifyDBNodesParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbnodes_parameters_with_options_async(request, runtime)

    def modify_global_database_network_with_options(
        self,
        request: polardb_20170801_models.ModifyGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalDatabaseNetworkResponse:
        """
        @summary Modifies a Global Database Network (GDN).
        
        @param request: ModifyGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdndescription):
            query['GDNDescription'] = request.gdndescription
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalDatabaseNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_database_network_with_options_async(
        self,
        request: polardb_20170801_models.ModifyGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalDatabaseNetworkResponse:
        """
        @summary Modifies a Global Database Network (GDN).
        
        @param request: ModifyGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gdndescription):
            query['GDNDescription'] = request.gdndescription
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalDatabaseNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_database_network(
        self,
        request: polardb_20170801_models.ModifyGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.ModifyGlobalDatabaseNetworkResponse:
        """
        @summary Modifies a Global Database Network (GDN).
        
        @param request: ModifyGlobalDatabaseNetworkRequest
        @return: ModifyGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_database_network_with_options(request, runtime)

    async def modify_global_database_network_async(
        self,
        request: polardb_20170801_models.ModifyGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.ModifyGlobalDatabaseNetworkResponse:
        """
        @summary Modifies a Global Database Network (GDN).
        
        @param request: ModifyGlobalDatabaseNetworkRequest
        @return: ModifyGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_database_network_with_options_async(request, runtime)

    def modify_global_security_ipgroup_with_options(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies an IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_with_options_async(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies an IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gip_list):
            query['GIpList'] = request.gip_list
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies an IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_with_options(request, runtime)

    async def modify_global_security_ipgroup_async(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupResponse:
        """
        @summary Modifies an IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRequest
        @return: ModifyGlobalSecurityIPGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_with_options_async(request, runtime)

    def modify_global_security_ipgroup_name_with_options(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalSecurityIPGroupNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_name_with_options_async(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupName',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalSecurityIPGroupNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_name(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_name_with_options(request, runtime)

    async def modify_global_security_ipgroup_name_async(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupNameResponse:
        """
        @summary Modifies the name of a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupNameRequest
        @return: ModifyGlobalSecurityIPGroupNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_name_with_options_async(request, runtime)

    def modify_global_security_ipgroup_relation_with_options(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the relationship between a cluster and a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupRelation',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_relation_with_options_async(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the relationship between a cluster and a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGlobalSecurityIPGroupRelation',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_relation(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the relationship between a cluster and a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_global_security_ipgroup_relation_with_options(request, runtime)

    async def modify_global_security_ipgroup_relation_async(
        self,
        request: polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> polardb_20170801_models.ModifyGlobalSecurityIPGroupRelationResponse:
        """
        @summary Modifies the relationship between a cluster and a global IP whitelist template.
        
        @param request: ModifyGlobalSecurityIPGroupRelationRequest
        @return: ModifyGlobalSecurityIPGroupRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_security_ipgroup_relation_with_options_async(request, runtime)

    def modify_log_backup_policy_with_options(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the retention policy of the log backups in a PolarDB cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.log_backup_another_region_region):
            query['LogBackupAnotherRegionRegion'] = request.log_backup_another_region_region
        if not UtilClient.is_unset(request.log_backup_another_region_retention_period):
            query['LogBackupAnotherRegionRetentionPeriod'] = request.log_backup_another_region_retention_period
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
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
            action='ModifyLogBackupPolicy',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyLogBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the retention policy of the log backups in a PolarDB cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.log_backup_another_region_region):
            query['LogBackupAnotherRegionRegion'] = request.log_backup_another_region_region
        if not UtilClient.is_unset(request.log_backup_another_region_retention_period):
            query['LogBackupAnotherRegionRetentionPeriod'] = request.log_backup_another_region_retention_period
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
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
            action='ModifyLogBackupPolicy',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyLogBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_backup_policy(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the retention policy of the log backups in a PolarDB cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @return: ModifyLogBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_log_backup_policy_with_options(request, runtime)

    async def modify_log_backup_policy_async(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        """
        @summary Modifies the retention policy of the log backups in a PolarDB cluster.
        
        @param request: ModifyLogBackupPolicyRequest
        @return: ModifyLogBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_backup_policy_with_options_async(request, runtime)

    def modify_masking_rules_with_options(
        self,
        request: polardb_20170801_models.ModifyMaskingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyMaskingRulesResponse:
        """
        @summary Modifies or adds a data masking rule.
        
        @param request: ModifyMaskingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMaskingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        if not UtilClient.is_unset(request.rule_version):
            query['RuleVersion'] = request.rule_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMaskingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyMaskingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_masking_rules_with_options_async(
        self,
        request: polardb_20170801_models.ModifyMaskingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyMaskingRulesResponse:
        """
        @summary Modifies or adds a data masking rule.
        
        @param request: ModifyMaskingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMaskingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.rule_config):
            query['RuleConfig'] = request.rule_config
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_name_list):
            query['RuleNameList'] = request.rule_name_list
        if not UtilClient.is_unset(request.rule_version):
            query['RuleVersion'] = request.rule_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMaskingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyMaskingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_masking_rules(
        self,
        request: polardb_20170801_models.ModifyMaskingRulesRequest,
    ) -> polardb_20170801_models.ModifyMaskingRulesResponse:
        """
        @summary Modifies or adds a data masking rule.
        
        @param request: ModifyMaskingRulesRequest
        @return: ModifyMaskingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_masking_rules_with_options(request, runtime)

    async def modify_masking_rules_async(
        self,
        request: polardb_20170801_models.ModifyMaskingRulesRequest,
    ) -> polardb_20170801_models.ModifyMaskingRulesResponse:
        """
        @summary Modifies or adds a data masking rule.
        
        @param request: ModifyMaskingRulesRequest
        @return: ModifyMaskingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_masking_rules_with_options_async(request, runtime)

    def modify_pending_maintenance_action_with_options(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        """
        @summary Modifies the switching time of a pending event.
        
        @param request: ModifyPendingMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPendingMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPendingMaintenanceAction',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyPendingMaintenanceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_pending_maintenance_action_with_options_async(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        """
        @summary Modifies the switching time of a pending event.
        
        @param request: ModifyPendingMaintenanceActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPendingMaintenanceActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPendingMaintenanceAction',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ModifyPendingMaintenanceActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_pending_maintenance_action(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        """
        @summary Modifies the switching time of a pending event.
        
        @param request: ModifyPendingMaintenanceActionRequest
        @return: ModifyPendingMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_pending_maintenance_action_with_options(request, runtime)

    async def modify_pending_maintenance_action_async(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        """
        @summary Modifies the switching time of a pending event.
        
        @param request: ModifyPendingMaintenanceActionRequest
        @return: ModifyPendingMaintenanceActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_pending_maintenance_action_with_options_async(request, runtime)

    def open_aitask_with_options(
        self,
        request: polardb_20170801_models.OpenAITaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.OpenAITaskResponse:
        """
        @summary Enables the PolarDB for AI feature for a cluster.
        
        @param request: OpenAITaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAITaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAITask',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.OpenAITaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_aitask_with_options_async(
        self,
        request: polardb_20170801_models.OpenAITaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.OpenAITaskResponse:
        """
        @summary Enables the PolarDB for AI feature for a cluster.
        
        @param request: OpenAITaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAITaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAITask',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.OpenAITaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_aitask(
        self,
        request: polardb_20170801_models.OpenAITaskRequest,
    ) -> polardb_20170801_models.OpenAITaskResponse:
        """
        @summary Enables the PolarDB for AI feature for a cluster.
        
        @param request: OpenAITaskRequest
        @return: OpenAITaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_aitask_with_options(request, runtime)

    async def open_aitask_async(
        self,
        request: polardb_20170801_models.OpenAITaskRequest,
    ) -> polardb_20170801_models.OpenAITaskResponse:
        """
        @summary Enables the PolarDB for AI feature for a cluster.
        
        @param request: OpenAITaskRequest
        @return: OpenAITaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_aitask_with_options_async(request, runtime)

    def refresh_dbcluster_storage_usage_with_options(
        self,
        request: polardb_20170801_models.RefreshDBClusterStorageUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RefreshDBClusterStorageUsageResponse:
        """
        @summary Updates the storage usage of a cluster.
        
        @param request: RefreshDBClusterStorageUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshDBClusterStorageUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sync_real_time):
            query['SyncRealTime'] = request.sync_real_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDBClusterStorageUsage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RefreshDBClusterStorageUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_dbcluster_storage_usage_with_options_async(
        self,
        request: polardb_20170801_models.RefreshDBClusterStorageUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RefreshDBClusterStorageUsageResponse:
        """
        @summary Updates the storage usage of a cluster.
        
        @param request: RefreshDBClusterStorageUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshDBClusterStorageUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sync_real_time):
            query['SyncRealTime'] = request.sync_real_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDBClusterStorageUsage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RefreshDBClusterStorageUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_dbcluster_storage_usage(
        self,
        request: polardb_20170801_models.RefreshDBClusterStorageUsageRequest,
    ) -> polardb_20170801_models.RefreshDBClusterStorageUsageResponse:
        """
        @summary Updates the storage usage of a cluster.
        
        @param request: RefreshDBClusterStorageUsageRequest
        @return: RefreshDBClusterStorageUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_dbcluster_storage_usage_with_options(request, runtime)

    async def refresh_dbcluster_storage_usage_async(
        self,
        request: polardb_20170801_models.RefreshDBClusterStorageUsageRequest,
    ) -> polardb_20170801_models.RefreshDBClusterStorageUsageResponse:
        """
        @summary Updates the storage usage of a cluster.
        
        @param request: RefreshDBClusterStorageUsageRequest
        @return: RefreshDBClusterStorageUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_dbcluster_storage_usage_with_options_async(request, runtime)

    def remove_dbcluster_from_gdnwith_options(
        self,
        request: polardb_20170801_models.RemoveDBClusterFromGDNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RemoveDBClusterFromGDNResponse:
        """
        @summary Removes a secondary cluster from a GDN.
        
        @description >  You cannot remove the primary cluster from a GDN.
        
        @param request: RemoveDBClusterFromGDNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDBClusterFromGDNResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDBClusterFromGDN',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RemoveDBClusterFromGDNResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_dbcluster_from_gdnwith_options_async(
        self,
        request: polardb_20170801_models.RemoveDBClusterFromGDNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RemoveDBClusterFromGDNResponse:
        """
        @summary Removes a secondary cluster from a GDN.
        
        @description >  You cannot remove the primary cluster from a GDN.
        
        @param request: RemoveDBClusterFromGDNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDBClusterFromGDNResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDBClusterFromGDN',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RemoveDBClusterFromGDNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_dbcluster_from_gdn(
        self,
        request: polardb_20170801_models.RemoveDBClusterFromGDNRequest,
    ) -> polardb_20170801_models.RemoveDBClusterFromGDNResponse:
        """
        @summary Removes a secondary cluster from a GDN.
        
        @description >  You cannot remove the primary cluster from a GDN.
        
        @param request: RemoveDBClusterFromGDNRequest
        @return: RemoveDBClusterFromGDNResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_dbcluster_from_gdnwith_options(request, runtime)

    async def remove_dbcluster_from_gdn_async(
        self,
        request: polardb_20170801_models.RemoveDBClusterFromGDNRequest,
    ) -> polardb_20170801_models.RemoveDBClusterFromGDNResponse:
        """
        @summary Removes a secondary cluster from a GDN.
        
        @description >  You cannot remove the primary cluster from a GDN.
        
        @param request: RemoveDBClusterFromGDNRequest
        @return: RemoveDBClusterFromGDNResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_dbcluster_from_gdnwith_options_async(request, runtime)

    def reset_account_with_options(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ResetAccountResponse:
        """
        @summary Resets the permissions of a privileged account for a PolarDB cluster.
        
        @description >- Only PolarDB for MySQL clusters support this operation.
        >- If the privileged account of your cluster encounters exceptions, you can call this operation to reset the permissions. For example, the permissions are accidentally revoked.
        
        @param request: ResetAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
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
            action='ResetAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ResetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_with_options_async(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ResetAccountResponse:
        """
        @summary Resets the permissions of a privileged account for a PolarDB cluster.
        
        @description >- Only PolarDB for MySQL clusters support this operation.
        >- If the privileged account of your cluster encounters exceptions, you can call this operation to reset the permissions. For example, the permissions are accidentally revoked.
        
        @param request: ResetAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
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
            action='ResetAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ResetAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
    ) -> polardb_20170801_models.ResetAccountResponse:
        """
        @summary Resets the permissions of a privileged account for a PolarDB cluster.
        
        @description >- Only PolarDB for MySQL clusters support this operation.
        >- If the privileged account of your cluster encounters exceptions, you can call this operation to reset the permissions. For example, the permissions are accidentally revoked.
        
        @param request: ResetAccountRequest
        @return: ResetAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    async def reset_account_async(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
    ) -> polardb_20170801_models.ResetAccountResponse:
        """
        @summary Resets the permissions of a privileged account for a PolarDB cluster.
        
        @description >- Only PolarDB for MySQL clusters support this operation.
        >- If the privileged account of your cluster encounters exceptions, you can call this operation to reset the permissions. For example, the permissions are accidentally revoked.
        
        @param request: ResetAccountRequest
        @return: ResetAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_with_options_async(request, runtime)

    def reset_global_database_network_with_options(
        self,
        request: polardb_20170801_models.ResetGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ResetGlobalDatabaseNetworkResponse:
        """
        @summary Rebuilds a secondary cluster in a Global Database Network (GDN).
        
        @param request: ResetGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ResetGlobalDatabaseNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_global_database_network_with_options_async(
        self,
        request: polardb_20170801_models.ResetGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ResetGlobalDatabaseNetworkResponse:
        """
        @summary Rebuilds a secondary cluster in a Global Database Network (GDN).
        
        @param request: ResetGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.ResetGlobalDatabaseNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_global_database_network(
        self,
        request: polardb_20170801_models.ResetGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.ResetGlobalDatabaseNetworkResponse:
        """
        @summary Rebuilds a secondary cluster in a Global Database Network (GDN).
        
        @param request: ResetGlobalDatabaseNetworkRequest
        @return: ResetGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_global_database_network_with_options(request, runtime)

    async def reset_global_database_network_async(
        self,
        request: polardb_20170801_models.ResetGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.ResetGlobalDatabaseNetworkResponse:
        """
        @summary Rebuilds a secondary cluster in a Global Database Network (GDN).
        
        @param request: ResetGlobalDatabaseNetworkRequest
        @return: ResetGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_global_database_network_with_options_async(request, runtime)

    def restart_dblink_with_options(
        self,
        request: polardb_20170801_models.RestartDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestartDBLinkResponse:
        """
        @summary Restarts database links.
        
        @param request: RestartDBLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBLinkResponse
        """
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBLink',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RestartDBLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dblink_with_options_async(
        self,
        request: polardb_20170801_models.RestartDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestartDBLinkResponse:
        """
        @summary Restarts database links.
        
        @param request: RestartDBLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBLinkResponse
        """
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
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBLink',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RestartDBLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dblink(
        self,
        request: polardb_20170801_models.RestartDBLinkRequest,
    ) -> polardb_20170801_models.RestartDBLinkResponse:
        """
        @summary Restarts database links.
        
        @param request: RestartDBLinkRequest
        @return: RestartDBLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dblink_with_options(request, runtime)

    async def restart_dblink_async(
        self,
        request: polardb_20170801_models.RestartDBLinkRequest,
    ) -> polardb_20170801_models.RestartDBLinkResponse:
        """
        @summary Restarts database links.
        
        @param request: RestartDBLinkRequest
        @return: RestartDBLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dblink_with_options_async(request, runtime)

    def restart_dbnode_with_options(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        """
        @summary Restarts a node in a PolarDB cluster.
        
        @param request: RestartDBNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
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
            action='RestartDBNode',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RestartDBNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbnode_with_options_async(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        """
        @summary Restarts a node in a PolarDB cluster.
        
        @param request: RestartDBNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbnode_id):
            query['DBNodeId'] = request.dbnode_id
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
            action='RestartDBNode',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RestartDBNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbnode(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        """
        @summary Restarts a node in a PolarDB cluster.
        
        @param request: RestartDBNodeRequest
        @return: RestartDBNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbnode_with_options(request, runtime)

    async def restart_dbnode_async(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        """
        @summary Restarts a node in a PolarDB cluster.
        
        @param request: RestartDBNodeRequest
        @return: RestartDBNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbnode_with_options_async(request, runtime)

    def restore_table_with_options(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestoreTableResponse:
        """
        @summary Restores PolarDB databases and tables.
        
        @param request: RestoreTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
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
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.table_meta):
            query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreTable',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RestoreTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_table_with_options_async(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestoreTableResponse:
        """
        @summary Restores PolarDB databases and tables.
        
        @param request: RestoreTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestoreTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
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
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.table_meta):
            query['TableMeta'] = request.table_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreTable',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RestoreTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_table(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
    ) -> polardb_20170801_models.RestoreTableResponse:
        """
        @summary Restores PolarDB databases and tables.
        
        @param request: RestoreTableRequest
        @return: RestoreTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    async def restore_table_async(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
    ) -> polardb_20170801_models.RestoreTableResponse:
        """
        @summary Restores PolarDB databases and tables.
        
        @param request: RestoreTableRequest
        @return: RestoreTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restore_table_with_options_async(request, runtime)

    def revoke_account_privilege_with_options(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        """
        @summary Revokes the access permissions on one or more databases from a specified PolarDB standard account.
        
        @param request: RevokeAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='RevokeAccountPrivilege',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RevokeAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_account_privilege_with_options_async(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        """
        @summary Revokes the access permissions on one or more databases from a specified PolarDB standard account.
        
        @param request: RevokeAccountPrivilegeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeAccountPrivilegeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
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
            action='RevokeAccountPrivilege',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.RevokeAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_account_privilege(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        """
        @summary Revokes the access permissions on one or more databases from a specified PolarDB standard account.
        
        @param request: RevokeAccountPrivilegeRequest
        @return: RevokeAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    async def revoke_account_privilege_async(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        """
        @summary Revokes the access permissions on one or more databases from a specified PolarDB standard account.
        
        @param request: RevokeAccountPrivilegeRequest
        @return: RevokeAccountPrivilegeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_account_privilege_with_options_async(request, runtime)

    def switch_over_global_database_network_with_options(
        self,
        request: polardb_20170801_models.SwitchOverGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.SwitchOverGlobalDatabaseNetworkResponse:
        """
        @param request: SwitchOverGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchOverGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.forced):
            query['Forced'] = request.forced
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchOverGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.SwitchOverGlobalDatabaseNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_over_global_database_network_with_options_async(
        self,
        request: polardb_20170801_models.SwitchOverGlobalDatabaseNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.SwitchOverGlobalDatabaseNetworkResponse:
        """
        @param request: SwitchOverGlobalDatabaseNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchOverGlobalDatabaseNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.forced):
            query['Forced'] = request.forced
        if not UtilClient.is_unset(request.gdnid):
            query['GDNId'] = request.gdnid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchOverGlobalDatabaseNetwork',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.SwitchOverGlobalDatabaseNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_over_global_database_network(
        self,
        request: polardb_20170801_models.SwitchOverGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.SwitchOverGlobalDatabaseNetworkResponse:
        """
        @param request: SwitchOverGlobalDatabaseNetworkRequest
        @return: SwitchOverGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_over_global_database_network_with_options(request, runtime)

    async def switch_over_global_database_network_async(
        self,
        request: polardb_20170801_models.SwitchOverGlobalDatabaseNetworkRequest,
    ) -> polardb_20170801_models.SwitchOverGlobalDatabaseNetworkResponse:
        """
        @param request: SwitchOverGlobalDatabaseNetworkRequest
        @return: SwitchOverGlobalDatabaseNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_over_global_database_network_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
    ) -> polardb_20170801_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
    ) -> polardb_20170801_models.TagResourcesResponse:
        """
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def temp_modify_dbnode_with_options(
        self,
        request: polardb_20170801_models.TempModifyDBNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TempModifyDBNodeResponse:
        """
        @summary Temporarily upgrades the configuration of a PolarDB cluster or adds one or more nodes to a cluster.
        
        @param request: TempModifyDBNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TempModifyDBNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode):
            query['DBNode'] = request.dbnode
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempModifyDBNode',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.TempModifyDBNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def temp_modify_dbnode_with_options_async(
        self,
        request: polardb_20170801_models.TempModifyDBNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TempModifyDBNodeResponse:
        """
        @summary Temporarily upgrades the configuration of a PolarDB cluster or adds one or more nodes to a cluster.
        
        @param request: TempModifyDBNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TempModifyDBNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbnode):
            query['DBNode'] = request.dbnode
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TempModifyDBNode',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.TempModifyDBNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def temp_modify_dbnode(
        self,
        request: polardb_20170801_models.TempModifyDBNodeRequest,
    ) -> polardb_20170801_models.TempModifyDBNodeResponse:
        """
        @summary Temporarily upgrades the configuration of a PolarDB cluster or adds one or more nodes to a cluster.
        
        @param request: TempModifyDBNodeRequest
        @return: TempModifyDBNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.temp_modify_dbnode_with_options(request, runtime)

    async def temp_modify_dbnode_async(
        self,
        request: polardb_20170801_models.TempModifyDBNodeRequest,
    ) -> polardb_20170801_models.TempModifyDBNodeResponse:
        """
        @summary Temporarily upgrades the configuration of a PolarDB cluster or adds one or more nodes to a cluster.
        
        @param request: TempModifyDBNodeRequest
        @return: TempModifyDBNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.temp_modify_dbnode_with_options_async(request, runtime)

    def transform_dbcluster_pay_type_with_options(
        self,
        request: polardb_20170801_models.TransformDBClusterPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TransformDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of a PolarDB cluster.
        
        @description >    PolarDB clusters support the subscription and pay-as-you-go billing methods. You can change the billing method from subscription to pay-as-you-go or from pay-as-you-go to subscription based on your business requirements. For more information, see [Change the billing method from subscription to pay-as-you-go](https://help.aliyun.com/document_detail/172886.html) and [Change the billing method from pay-as-you-go to subscription](https://help.aliyun.com/document_detail/84076.html).
        >   You cannot change the billing method from pay-as-you-go to subscription if your account balance is insufficient.
        >   If you change the billing method from subscription to pay-as-you-go, the system automatically refunds the balance of the prepaid subscription fees.
        
        @param request: TransformDBClusterPayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformDBClusterPayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformDBClusterPayType',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.TransformDBClusterPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_dbcluster_pay_type_with_options_async(
        self,
        request: polardb_20170801_models.TransformDBClusterPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TransformDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of a PolarDB cluster.
        
        @description >    PolarDB clusters support the subscription and pay-as-you-go billing methods. You can change the billing method from subscription to pay-as-you-go or from pay-as-you-go to subscription based on your business requirements. For more information, see [Change the billing method from subscription to pay-as-you-go](https://help.aliyun.com/document_detail/172886.html) and [Change the billing method from pay-as-you-go to subscription](https://help.aliyun.com/document_detail/84076.html).
        >   You cannot change the billing method from pay-as-you-go to subscription if your account balance is insufficient.
        >   If you change the billing method from subscription to pay-as-you-go, the system automatically refunds the balance of the prepaid subscription fees.
        
        @param request: TransformDBClusterPayTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformDBClusterPayTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformDBClusterPayType',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.TransformDBClusterPayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_dbcluster_pay_type(
        self,
        request: polardb_20170801_models.TransformDBClusterPayTypeRequest,
    ) -> polardb_20170801_models.TransformDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of a PolarDB cluster.
        
        @description >    PolarDB clusters support the subscription and pay-as-you-go billing methods. You can change the billing method from subscription to pay-as-you-go or from pay-as-you-go to subscription based on your business requirements. For more information, see [Change the billing method from subscription to pay-as-you-go](https://help.aliyun.com/document_detail/172886.html) and [Change the billing method from pay-as-you-go to subscription](https://help.aliyun.com/document_detail/84076.html).
        >   You cannot change the billing method from pay-as-you-go to subscription if your account balance is insufficient.
        >   If you change the billing method from subscription to pay-as-you-go, the system automatically refunds the balance of the prepaid subscription fees.
        
        @param request: TransformDBClusterPayTypeRequest
        @return: TransformDBClusterPayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.transform_dbcluster_pay_type_with_options(request, runtime)

    async def transform_dbcluster_pay_type_async(
        self,
        request: polardb_20170801_models.TransformDBClusterPayTypeRequest,
    ) -> polardb_20170801_models.TransformDBClusterPayTypeResponse:
        """
        @summary Changes the billing method of a PolarDB cluster.
        
        @description >    PolarDB clusters support the subscription and pay-as-you-go billing methods. You can change the billing method from subscription to pay-as-you-go or from pay-as-you-go to subscription based on your business requirements. For more information, see [Change the billing method from subscription to pay-as-you-go](https://help.aliyun.com/document_detail/172886.html) and [Change the billing method from pay-as-you-go to subscription](https://help.aliyun.com/document_detail/84076.html).
        >   You cannot change the billing method from pay-as-you-go to subscription if your account balance is insufficient.
        >   If you change the billing method from subscription to pay-as-you-go, the system automatically refunds the balance of the prepaid subscription fees.
        
        @param request: TransformDBClusterPayTypeRequest
        @return: TransformDBClusterPayTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.transform_dbcluster_pay_type_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from PolarDB clusters.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from PolarDB clusters.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from PolarDB clusters.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from PolarDB clusters.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_dbcluster_version_with_options(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        """
        @summary Upgrades the kernel version of a PolarDB for MySQL cluster.
        
        @description >   You can update only the revision version of a PolarDB for MySQL cluster, for example, from 8.0.1.1.3 to 8.0.1.1.4.
        >   You can use only your Alibaba Cloud account to create scheduled tasks that update the kernel version of a PolarDB for MySQL cluster. RAM users are not authorized to update the kernel version of a PolarDB for MySQL cluster.
        
        @param request: UpgradeDBClusterVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBClusterVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_dbrevision_version_code):
            query['TargetDBRevisionVersionCode'] = request.target_dbrevision_version_code
        if not UtilClient.is_unset(request.target_proxy_revision_version_code):
            query['TargetProxyRevisionVersionCode'] = request.target_proxy_revision_version_code
        if not UtilClient.is_unset(request.upgrade_label):
            query['UpgradeLabel'] = request.upgrade_label
        if not UtilClient.is_unset(request.upgrade_policy):
            query['UpgradePolicy'] = request.upgrade_policy
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBClusterVersion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.UpgradeDBClusterVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbcluster_version_with_options_async(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        """
        @summary Upgrades the kernel version of a PolarDB for MySQL cluster.
        
        @description >   You can update only the revision version of a PolarDB for MySQL cluster, for example, from 8.0.1.1.3 to 8.0.1.1.4.
        >   You can use only your Alibaba Cloud account to create scheduled tasks that update the kernel version of a PolarDB for MySQL cluster. RAM users are not authorized to update the kernel version of a PolarDB for MySQL cluster.
        
        @param request: UpgradeDBClusterVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBClusterVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.from_time_service):
            query['FromTimeService'] = request.from_time_service
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.planned_end_time):
            query['PlannedEndTime'] = request.planned_end_time
        if not UtilClient.is_unset(request.planned_start_time):
            query['PlannedStartTime'] = request.planned_start_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.target_dbrevision_version_code):
            query['TargetDBRevisionVersionCode'] = request.target_dbrevision_version_code
        if not UtilClient.is_unset(request.target_proxy_revision_version_code):
            query['TargetProxyRevisionVersionCode'] = request.target_proxy_revision_version_code
        if not UtilClient.is_unset(request.upgrade_label):
            query['UpgradeLabel'] = request.upgrade_label
        if not UtilClient.is_unset(request.upgrade_policy):
            query['UpgradePolicy'] = request.upgrade_policy
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBClusterVersion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_20170801_models.UpgradeDBClusterVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbcluster_version(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        """
        @summary Upgrades the kernel version of a PolarDB for MySQL cluster.
        
        @description >   You can update only the revision version of a PolarDB for MySQL cluster, for example, from 8.0.1.1.3 to 8.0.1.1.4.
        >   You can use only your Alibaba Cloud account to create scheduled tasks that update the kernel version of a PolarDB for MySQL cluster. RAM users are not authorized to update the kernel version of a PolarDB for MySQL cluster.
        
        @param request: UpgradeDBClusterVersionRequest
        @return: UpgradeDBClusterVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbcluster_version_with_options(request, runtime)

    async def upgrade_dbcluster_version_async(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        """
        @summary Upgrades the kernel version of a PolarDB for MySQL cluster.
        
        @description >   You can update only the revision version of a PolarDB for MySQL cluster, for example, from 8.0.1.1.3 to 8.0.1.1.4.
        >   You can use only your Alibaba Cloud account to create scheduled tasks that update the kernel version of a PolarDB for MySQL cluster. RAM users are not authorized to update the kernel version of a PolarDB for MySQL cluster.
        
        @param request: UpgradeDBClusterVersionRequest
        @return: UpgradeDBClusterVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbcluster_version_with_options_async(request, runtime)
