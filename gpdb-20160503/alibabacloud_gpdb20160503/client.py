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

    def allocate_instance_public_connection_with_options(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        """
        You can call this operation to apply for a public endpoint for an AnalyticDB for PostgreSQL instance. Both the primary and instance endpoints of an AnalyticDB for PostgreSQL instance can be public endpoints. For more information, see [Endpoints of an instance and its primary coordinator node](~~204879~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        """
        You can call this operation to apply for a public endpoint for an AnalyticDB for PostgreSQL instance. Both the primary and instance endpoints of an AnalyticDB for PostgreSQL instance can be public endpoints. For more information, see [Endpoints of an instance and its primary coordinator node](~~204879~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        """
        You can call this operation to apply for a public endpoint for an AnalyticDB for PostgreSQL instance. Both the primary and instance endpoints of an AnalyticDB for PostgreSQL instance can be public endpoints. For more information, see [Endpoints of an instance and its primary coordinator node](~~204879~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        """
        You can call this operation to apply for a public endpoint for an AnalyticDB for PostgreSQL instance. Both the primary and instance endpoints of an AnalyticDB for PostgreSQL instance can be public endpoints. For more information, see [Endpoints of an instance and its primary coordinator node](~~204879~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: gpdb_20160503_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: gpdb_20160503_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        Before you can use an AnalyticDB for PostgreSQL instance, you must create a privileged account for the instance.
        *   You can call this operation to create only privileged accounts. For information about how to create other types of accounts, see [Create a database account](~~50206~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: gpdb_20160503_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateAccountResponse:
        """
        Before you can use an AnalyticDB for PostgreSQL instance, you must create a privileged account for the instance.
        *   You can call this operation to create only privileged accounts. For information about how to create other types of accounts, see [Create a database account](~~50206~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: gpdb_20160503_models.CreateAccountRequest,
    ) -> gpdb_20160503_models.CreateAccountResponse:
        """
        Before you can use an AnalyticDB for PostgreSQL instance, you must create a privileged account for the instance.
        *   You can call this operation to create only privileged accounts. For information about how to create other types of accounts, see [Create a database account](~~50206~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: gpdb_20160503_models.CreateAccountRequest,
    ) -> gpdb_20160503_models.CreateAccountResponse:
        """
        Before you can use an AnalyticDB for PostgreSQL instance, you must create a privileged account for the instance.
        *   You can call this operation to create only privileged accounts. For information about how to create other types of accounts, see [Create a database account](~~50206~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_collection_with_options(
        self,
        request: gpdb_20160503_models.CreateCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metadata):
            query['Metadata'] = request.metadata
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parser):
            query['Parser'] = request.parser
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_collection_with_options_async(
        self,
        request: gpdb_20160503_models.CreateCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metadata):
            query['Metadata'] = request.metadata
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parser):
            query['Parser'] = request.parser
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_collection(
        self,
        request: gpdb_20160503_models.CreateCollectionRequest,
    ) -> gpdb_20160503_models.CreateCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_collection_with_options(request, runtime)

    async def create_collection_async(
        self,
        request: gpdb_20160503_models.CreateCollectionRequest,
    ) -> gpdb_20160503_models.CreateCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_collection_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        """
        You can call this operation when you need to create AnalyticDB for PostgreSQL instances to meet the requirements of new applications or services.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_sample_data):
            query['CreateSampleData'] = request.create_sample_data
        if not UtilClient.is_unset(request.dbinstance_category):
            query['DBInstanceCategory'] = request.dbinstance_category
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not UtilClient.is_unset(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not UtilClient.is_unset(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.serverless_mode):
            query['ServerlessMode'] = request.serverless_mode
        if not UtilClient.is_unset(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        if not UtilClient.is_unset(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        """
        You can call this operation when you need to create AnalyticDB for PostgreSQL instances to meet the requirements of new applications or services.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_sample_data):
            query['CreateSampleData'] = request.create_sample_data
        if not UtilClient.is_unset(request.dbinstance_category):
            query['DBInstanceCategory'] = request.dbinstance_category
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not UtilClient.is_unset(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not UtilClient.is_unset(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.serverless_mode):
            query['ServerlessMode'] = request.serverless_mode
        if not UtilClient.is_unset(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        if not UtilClient.is_unset(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        """
        You can call this operation when you need to create AnalyticDB for PostgreSQL instances to meet the requirements of new applications or services.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        """
        You can call this operation when you need to create AnalyticDB for PostgreSQL instances to meet the requirements of new applications or services.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_dbinstance_plan_with_options(
        self,
        request: gpdb_20160503_models.CreateDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDBInstancePlanResponse:
        """
        The plan management feature is supported only for pay-as-you-go instances.
        *   When you change the compute node specifications or change the number of compute nodes, transient connections may occur. We recommend that you perform these operations during off-peak hours.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: CreateDBInstancePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not UtilClient.is_unset(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_plan_with_options_async(
        self,
        request: gpdb_20160503_models.CreateDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDBInstancePlanResponse:
        """
        The plan management feature is supported only for pay-as-you-go instances.
        *   When you change the compute node specifications or change the number of compute nodes, transient connections may occur. We recommend that you perform these operations during off-peak hours.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: CreateDBInstancePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not UtilClient.is_unset(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstancePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance_plan(
        self,
        request: gpdb_20160503_models.CreateDBInstancePlanRequest,
    ) -> gpdb_20160503_models.CreateDBInstancePlanResponse:
        """
        The plan management feature is supported only for pay-as-you-go instances.
        *   When you change the compute node specifications or change the number of compute nodes, transient connections may occur. We recommend that you perform these operations during off-peak hours.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: CreateDBInstancePlanRequest
        @return: CreateDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_plan_with_options(request, runtime)

    async def create_dbinstance_plan_async(
        self,
        request: gpdb_20160503_models.CreateDBInstancePlanRequest,
    ) -> gpdb_20160503_models.CreateDBInstancePlanResponse:
        """
        The plan management feature is supported only for pay-as-you-go instances.
        *   When you change the compute node specifications or change the number of compute nodes, transient connections may occur. We recommend that you perform these operations during off-peak hours.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: CreateDBInstancePlanRequest
        @return: CreateDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_plan_with_options_async(request, runtime)

    def create_document_collection_with_options(
        self,
        request: gpdb_20160503_models.CreateDocumentCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDocumentCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.embedding_model):
            query['EmbeddingModel'] = request.embedding_model
        if not UtilClient.is_unset(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metadata):
            query['Metadata'] = request.metadata
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parser):
            query['Parser'] = request.parser
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDocumentCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDocumentCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_document_collection_with_options_async(
        self,
        request: gpdb_20160503_models.CreateDocumentCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDocumentCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.embedding_model):
            query['EmbeddingModel'] = request.embedding_model
        if not UtilClient.is_unset(request.full_text_retrieval_fields):
            query['FullTextRetrievalFields'] = request.full_text_retrieval_fields
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metadata):
            query['Metadata'] = request.metadata
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parser):
            query['Parser'] = request.parser
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDocumentCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDocumentCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_document_collection(
        self,
        request: gpdb_20160503_models.CreateDocumentCollectionRequest,
    ) -> gpdb_20160503_models.CreateDocumentCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_document_collection_with_options(request, runtime)

    async def create_document_collection_async(
        self,
        request: gpdb_20160503_models.CreateDocumentCollectionRequest,
    ) -> gpdb_20160503_models.CreateDocumentCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_document_collection_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: gpdb_20160503_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: gpdb_20160503_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: gpdb_20160503_models.CreateNamespaceRequest,
    ) -> gpdb_20160503_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: gpdb_20160503_models.CreateNamespaceRequest,
    ) -> gpdb_20160503_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_sample_data_with_options(
        self,
        request: gpdb_20160503_models.CreateSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateSampleDataResponse:
        """
        You can call this operation to load a sample dataset to an AnalyticDB for PostgreSQL instance. Then, you can execute query statements on the sample dataset to experience or test your instance. For more information about query statements, see [Dataset information and query examples](~~452277~~).
        ## Precautions
        - If your instance is in elastic storage mode, the sample dataset is supported only for V6.3.10.3 or later. If your instance is in Serverless mode, the sample dataset is supported only for V1.0.4.0 or later. For more information about how to update the minor engine version of an instance, see [Update the minor engine version](/help/en/analyticdb-for-postgresql/latest/upgrade-the-engine-version).
        - The sample dataset is about 10 GB in size. Make sure that your instance has sufficient storage space.
        - The sample dataset contains a database named `ADB_SampleData_TPCH`. Make sure that your instance does not have a database with the same name. Otherwise, the dataset may fail to be loaded.
        - It may take 6 to 8 minutes to load the sample dataset. During this period, operations on your instance such as adding nodes or changing node specifications may be affected.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSampleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sample_data_with_options_async(
        self,
        request: gpdb_20160503_models.CreateSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateSampleDataResponse:
        """
        You can call this operation to load a sample dataset to an AnalyticDB for PostgreSQL instance. Then, you can execute query statements on the sample dataset to experience or test your instance. For more information about query statements, see [Dataset information and query examples](~~452277~~).
        ## Precautions
        - If your instance is in elastic storage mode, the sample dataset is supported only for V6.3.10.3 or later. If your instance is in Serverless mode, the sample dataset is supported only for V1.0.4.0 or later. For more information about how to update the minor engine version of an instance, see [Update the minor engine version](/help/en/analyticdb-for-postgresql/latest/upgrade-the-engine-version).
        - The sample dataset is about 10 GB in size. Make sure that your instance has sufficient storage space.
        - The sample dataset contains a database named `ADB_SampleData_TPCH`. Make sure that your instance does not have a database with the same name. Otherwise, the dataset may fail to be loaded.
        - It may take 6 to 8 minutes to load the sample dataset. During this period, operations on your instance such as adding nodes or changing node specifications may be affected.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSampleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sample_data(
        self,
        request: gpdb_20160503_models.CreateSampleDataRequest,
    ) -> gpdb_20160503_models.CreateSampleDataResponse:
        """
        You can call this operation to load a sample dataset to an AnalyticDB for PostgreSQL instance. Then, you can execute query statements on the sample dataset to experience or test your instance. For more information about query statements, see [Dataset information and query examples](~~452277~~).
        ## Precautions
        - If your instance is in elastic storage mode, the sample dataset is supported only for V6.3.10.3 or later. If your instance is in Serverless mode, the sample dataset is supported only for V1.0.4.0 or later. For more information about how to update the minor engine version of an instance, see [Update the minor engine version](/help/en/analyticdb-for-postgresql/latest/upgrade-the-engine-version).
        - The sample dataset is about 10 GB in size. Make sure that your instance has sufficient storage space.
        - The sample dataset contains a database named `ADB_SampleData_TPCH`. Make sure that your instance does not have a database with the same name. Otherwise, the dataset may fail to be loaded.
        - It may take 6 to 8 minutes to load the sample dataset. During this period, operations on your instance such as adding nodes or changing node specifications may be affected.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSampleDataRequest
        @return: CreateSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sample_data_with_options(request, runtime)

    async def create_sample_data_async(
        self,
        request: gpdb_20160503_models.CreateSampleDataRequest,
    ) -> gpdb_20160503_models.CreateSampleDataResponse:
        """
        You can call this operation to load a sample dataset to an AnalyticDB for PostgreSQL instance. Then, you can execute query statements on the sample dataset to experience or test your instance. For more information about query statements, see [Dataset information and query examples](~~452277~~).
        ## Precautions
        - If your instance is in elastic storage mode, the sample dataset is supported only for V6.3.10.3 or later. If your instance is in Serverless mode, the sample dataset is supported only for V1.0.4.0 or later. For more information about how to update the minor engine version of an instance, see [Update the minor engine version](/help/en/analyticdb-for-postgresql/latest/upgrade-the-engine-version).
        - The sample dataset is about 10 GB in size. Make sure that your instance has sufficient storage space.
        - The sample dataset contains a database named `ADB_SampleData_TPCH`. Make sure that your instance does not have a database with the same name. Otherwise, the dataset may fail to be loaded.
        - It may take 6 to 8 minutes to load the sample dataset. During this period, operations on your instance such as adding nodes or changing node specifications may be affected.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSampleDataRequest
        @return: CreateSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sample_data_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: gpdb_20160503_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: gpdb_20160503_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_vector_index_with_options(
        self,
        request: gpdb_20160503_models.CreateVectorIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateVectorIndexResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVectorIndex',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateVectorIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vector_index_with_options_async(
        self,
        request: gpdb_20160503_models.CreateVectorIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateVectorIndexResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.hnsw_m):
            query['HnswM'] = request.hnsw_m
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pq_enable):
            query['PqEnable'] = request.pq_enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVectorIndex',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateVectorIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vector_index(
        self,
        request: gpdb_20160503_models.CreateVectorIndexRequest,
    ) -> gpdb_20160503_models.CreateVectorIndexResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vector_index_with_options(request, runtime)

    async def create_vector_index_async(
        self,
        request: gpdb_20160503_models.CreateVectorIndexRequest,
    ) -> gpdb_20160503_models.CreateVectorIndexResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vector_index_with_options_async(request, runtime)

    def delete_collection_with_options(
        self,
        request: gpdb_20160503_models.DeleteCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_collection_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_collection(
        self,
        request: gpdb_20160503_models.DeleteCollectionRequest,
    ) -> gpdb_20160503_models.DeleteCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_collection_with_options(request, runtime)

    async def delete_collection_async(
        self,
        request: gpdb_20160503_models.DeleteCollectionRequest,
    ) -> gpdb_20160503_models.DeleteCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_collection_with_options_async(request, runtime)

    def delete_collection_data_with_options(
        self,
        request: gpdb_20160503_models.DeleteCollectionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteCollectionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.collection_data):
            query['CollectionData'] = request.collection_data
        if not UtilClient.is_unset(request.collection_data_filter):
            query['CollectionDataFilter'] = request.collection_data_filter
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_collection_data_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteCollectionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteCollectionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.collection_data):
            query['CollectionData'] = request.collection_data
        if not UtilClient.is_unset(request.collection_data_filter):
            query['CollectionDataFilter'] = request.collection_data_filter
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteCollectionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_collection_data(
        self,
        request: gpdb_20160503_models.DeleteCollectionDataRequest,
    ) -> gpdb_20160503_models.DeleteCollectionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_collection_data_with_options(request, runtime)

    async def delete_collection_data_async(
        self,
        request: gpdb_20160503_models.DeleteCollectionDataRequest,
    ) -> gpdb_20160503_models.DeleteCollectionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_collection_data_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        """
        Subscription instances cannot be manually released. They are automatically released when they expire.
        *   You can call this operation to release pay-as-you-go instances only when they are in the **Running** state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        """
        Subscription instances cannot be manually released. They are automatically released when they expire.
        *   You can call this operation to release pay-as-you-go instances only when they are in the **Running** state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        """
        Subscription instances cannot be manually released. They are automatically released when they expire.
        *   You can call this operation to release pay-as-you-go instances only when they are in the **Running** state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        """
        Subscription instances cannot be manually released. They are automatically released when they expire.
        *   You can call this operation to release pay-as-you-go instances only when they are in the **Running** state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_dbinstance_plan_with_options(
        self,
        request: gpdb_20160503_models.DeleteDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstancePlanResponse:
        """
        If you no longer need a plan, you can call this operation to delete the plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstancePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_plan_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstancePlanResponse:
        """
        If you no longer need a plan, you can call this operation to delete the plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstancePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstancePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance_plan(
        self,
        request: gpdb_20160503_models.DeleteDBInstancePlanRequest,
    ) -> gpdb_20160503_models.DeleteDBInstancePlanResponse:
        """
        If you no longer need a plan, you can call this operation to delete the plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstancePlanRequest
        @return: DeleteDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_plan_with_options(request, runtime)

    async def delete_dbinstance_plan_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstancePlanRequest,
    ) -> gpdb_20160503_models.DeleteDBInstancePlanResponse:
        """
        If you no longer need a plan, you can call this operation to delete the plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteDBInstancePlanRequest
        @return: DeleteDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_plan_with_options_async(request, runtime)

    def delete_document_with_options(
        self,
        request: gpdb_20160503_models.DeleteDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        request: gpdb_20160503_models.DeleteDocumentRequest,
    ) -> gpdb_20160503_models.DeleteDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_document_with_options(request, runtime)

    async def delete_document_async(
        self,
        request: gpdb_20160503_models.DeleteDocumentRequest,
    ) -> gpdb_20160503_models.DeleteDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_document_with_options_async(request, runtime)

    def delete_document_collection_with_options(
        self,
        request: gpdb_20160503_models.DeleteDocumentCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDocumentCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocumentCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDocumentCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_collection_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteDocumentCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDocumentCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocumentCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDocumentCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document_collection(
        self,
        request: gpdb_20160503_models.DeleteDocumentCollectionRequest,
    ) -> gpdb_20160503_models.DeleteDocumentCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_document_collection_with_options(request, runtime)

    async def delete_document_collection_async(
        self,
        request: gpdb_20160503_models.DeleteDocumentCollectionRequest,
    ) -> gpdb_20160503_models.DeleteDocumentCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_document_collection_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: gpdb_20160503_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: gpdb_20160503_models.DeleteNamespaceRequest,
    ) -> gpdb_20160503_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: gpdb_20160503_models.DeleteNamespaceRequest,
    ) -> gpdb_20160503_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_vector_index_with_options(
        self,
        request: gpdb_20160503_models.DeleteVectorIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteVectorIndexResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVectorIndex',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteVectorIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vector_index_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteVectorIndexRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteVectorIndexResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVectorIndex',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteVectorIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vector_index(
        self,
        request: gpdb_20160503_models.DeleteVectorIndexRequest,
    ) -> gpdb_20160503_models.DeleteVectorIndexResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vector_index_with_options(request, runtime)

    async def delete_vector_index_async(
        self,
        request: gpdb_20160503_models.DeleteVectorIndexRequest,
    ) -> gpdb_20160503_models.DeleteVectorIndexResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vector_index_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        """
        This operation is called to query the information of the privileged account in an AnalyticDB for PostgreSQL instance, such as its state, description, and the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        """
        This operation is called to query the information of the privileged account in an AnalyticDB for PostgreSQL instance, such as its state, description, and the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        """
        This operation is called to query the information of the privileged account in an AnalyticDB for PostgreSQL instance, such as its state, description, and the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        """
        This operation is called to query the information of the privileged account in an AnalyticDB for PostgreSQL instance, such as its state, description, and the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_available_resources_with_options(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available resources within a zone.
        
        @param request: DescribeAvailableResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAvailableResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resources_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available resources within a zone.
        
        @param request: DescribeAvailableResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAvailableResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResources',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAvailableResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resources(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available resources within a zone.
        
        @param request: DescribeAvailableResourcesRequest
        @return: DescribeAvailableResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resources_with_options(request, runtime)

    async def describe_available_resources_async(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available resources within a zone.
        
        @param request: DescribeAvailableResourcesRequest
        @return: DescribeAvailableResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resources_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        """
        You can call this operation to query the backup settings of an AnalyticDB for PostgreSQL instance in elastic storage mode. Periodically backing data can prevent data loss. For more information about how to modify backup policies, see [ModifyBackupPolicy](~~210095~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        """
        You can call this operation to query the backup settings of an AnalyticDB for PostgreSQL instance in elastic storage mode. Periodically backing data can prevent data loss. For more information about how to modify backup policies, see [ModifyBackupPolicy](~~210095~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        """
        You can call this operation to query the backup settings of an AnalyticDB for PostgreSQL instance in elastic storage mode. Periodically backing data can prevent data loss. For more information about how to modify backup policies, see [ModifyBackupPolicy](~~210095~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        """
        You can call this operation to query the backup settings of an AnalyticDB for PostgreSQL instance in elastic storage mode. Periodically backing data can prevent data loss. For more information about how to modify backup policies, see [ModifyBackupPolicy](~~210095~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_collection_with_options(
        self,
        request: gpdb_20160503_models.DescribeCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_collection_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_collection(
        self,
        request: gpdb_20160503_models.DescribeCollectionRequest,
    ) -> gpdb_20160503_models.DescribeCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_collection_with_options(request, runtime)

    async def describe_collection_async(
        self,
        request: gpdb_20160503_models.DescribeCollectionRequest,
    ) -> gpdb_20160503_models.DescribeCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_collection_with_options_async(request, runtime)

    def describe_dbcluster_node_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterNodeResponse:
        """
        ##
        You can call this operation to query the information about coordinator and compute nodes in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBClusterNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNode',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_node_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterNodeResponse:
        """
        ##
        You can call this operation to query the information about coordinator and compute nodes in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBClusterNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNode',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_node(
        self,
        request: gpdb_20160503_models.DescribeDBClusterNodeRequest,
    ) -> gpdb_20160503_models.DescribeDBClusterNodeResponse:
        """
        ##
        You can call this operation to query the information about coordinator and compute nodes in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBClusterNodeRequest
        @return: DescribeDBClusterNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_node_with_options(request, runtime)

    async def describe_dbcluster_node_async(
        self,
        request: gpdb_20160503_models.DescribeDBClusterNodeRequest,
    ) -> gpdb_20160503_models.DescribeDBClusterNodeResponse:
        """
        ##
        You can call this operation to query the information about coordinator and compute nodes in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBClusterNodeRequest
        @return: DescribeDBClusterNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_node_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        """
        You can query monitoring information only within the last 30 days.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.nodes):
            query['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        """
        You can query monitoring information only within the last 30 days.
        
        @param request: DescribeDBClusterPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.nodes):
            query['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        """
        You can query monitoring information only within the last 30 days.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        """
        You can query monitoring information only within the last 30 days.
        
        @param request: DescribeDBClusterPerformanceRequest
        @return: DescribeDBClusterPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        """
        ##
        You can call this operation to query the information about an AnalyticDB for PostgreSQL instance, such as the instance type, network type, and instance state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        """
        ##
        You can call this operation to query the information about an AnalyticDB for PostgreSQL instance, such as the instance type, network type, and instance state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        """
        ##
        You can call this operation to query the information about an AnalyticDB for PostgreSQL instance, such as the instance type, network type, and instance state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        """
        ##
        You can call this operation to query the information about an AnalyticDB for PostgreSQL instance, such as the instance type, network type, and instance state.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_data_bloat_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataBloatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataBloatResponse:
        """
        You can call this operation to query the details of data bloat on an AnalyticDB for PostgreSQL instance in elastic storage mode. The minor version of the instance must be V6.3.10.1 or later. For more information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataBloatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataBloatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataBloat',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDataBloatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_data_bloat_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataBloatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataBloatResponse:
        """
        You can call this operation to query the details of data bloat on an AnalyticDB for PostgreSQL instance in elastic storage mode. The minor version of the instance must be V6.3.10.1 or later. For more information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataBloatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataBloatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataBloat',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDataBloatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_data_bloat(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataBloatRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataBloatResponse:
        """
        You can call this operation to query the details of data bloat on an AnalyticDB for PostgreSQL instance in elastic storage mode. The minor version of the instance must be V6.3.10.1 or later. For more information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataBloatRequest
        @return: DescribeDBInstanceDataBloatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_bloat_with_options(request, runtime)

    async def describe_dbinstance_data_bloat_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataBloatRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataBloatResponse:
        """
        You can call this operation to query the details of data bloat on an AnalyticDB for PostgreSQL instance in elastic storage mode. The minor version of the instance must be V6.3.10.1 or later. For more information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataBloatRequest
        @return: DescribeDBInstanceDataBloatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_data_bloat_with_options_async(request, runtime)

    def describe_dbinstance_data_skew_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataSkewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataSkewResponse:
        """
        To prevent data skew from affecting your database service, you can call this operation to query the details about data skew on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataSkewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataSkewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataSkew',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDataSkewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_data_skew_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataSkewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataSkewResponse:
        """
        To prevent data skew from affecting your database service, you can call this operation to query the details about data skew on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataSkewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataSkewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataSkew',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDataSkewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_data_skew(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataSkewRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataSkewResponse:
        """
        To prevent data skew from affecting your database service, you can call this operation to query the details about data skew on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataSkewRequest
        @return: DescribeDBInstanceDataSkewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_skew_with_options(request, runtime)

    async def describe_dbinstance_data_skew_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataSkewRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataSkewResponse:
        """
        To prevent data skew from affecting your database service, you can call this operation to query the details about data skew on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceDataSkewRequest
        @return: DescribeDBInstanceDataSkewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_data_skew_with_options_async(request, runtime)

    def describe_dbinstance_diagnosis_summary_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse:
        """
        You can call this operation to query the distribution and states of coordinator and compute nodes in an AnalyticDB for PostgreSQL instance.
        
        @param request: DescribeDBInstanceDiagnosisSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDiagnosisSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_preferd):
            query['RolePreferd'] = request.role_preferd
        if not UtilClient.is_unset(request.start_status):
            query['StartStatus'] = request.start_status
        if not UtilClient.is_unset(request.sync_mode):
            query['SyncMode'] = request.sync_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDiagnosisSummary',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_diagnosis_summary_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse:
        """
        You can call this operation to query the distribution and states of coordinator and compute nodes in an AnalyticDB for PostgreSQL instance.
        
        @param request: DescribeDBInstanceDiagnosisSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDiagnosisSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role_preferd):
            query['RolePreferd'] = request.role_preferd
        if not UtilClient.is_unset(request.start_status):
            query['StartStatus'] = request.start_status
        if not UtilClient.is_unset(request.sync_mode):
            query['SyncMode'] = request.sync_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDiagnosisSummary',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_diagnosis_summary(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse:
        """
        You can call this operation to query the distribution and states of coordinator and compute nodes in an AnalyticDB for PostgreSQL instance.
        
        @param request: DescribeDBInstanceDiagnosisSummaryRequest
        @return: DescribeDBInstanceDiagnosisSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_diagnosis_summary_with_options(request, runtime)

    async def describe_dbinstance_diagnosis_summary_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse:
        """
        You can call this operation to query the distribution and states of coordinator and compute nodes in an AnalyticDB for PostgreSQL instance.
        
        @param request: DescribeDBInstanceDiagnosisSummaryRequest
        @return: DescribeDBInstanceDiagnosisSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_diagnosis_summary_with_options_async(request, runtime)

    def describe_dbinstance_error_log_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceErrorLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceErrorLogResponse:
        """
        You can call this operation to query the error logs of an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceErrorLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceErrorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceErrorLog',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceErrorLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_error_log_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceErrorLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceErrorLogResponse:
        """
        You can call this operation to query the error logs of an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceErrorLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceErrorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.log_level):
            query['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceErrorLog',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceErrorLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_error_log(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceErrorLogRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceErrorLogResponse:
        """
        You can call this operation to query the error logs of an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceErrorLogRequest
        @return: DescribeDBInstanceErrorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_error_log_with_options(request, runtime)

    async def describe_dbinstance_error_log_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceErrorLogRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceErrorLogResponse:
        """
        You can call this operation to query the error logs of an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceErrorLogRequest
        @return: DescribeDBInstanceErrorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_error_log_with_options_async(request, runtime)

    def describe_dbinstance_iparray_list_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        """
        You can call this operation to query the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceIPArrayListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceIPArrayListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIPArrayList',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_iparray_list_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        """
        You can call this operation to query the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceIPArrayListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceIPArrayListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIPArrayList',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_iparray_list(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        """
        You can call this operation to query the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceIPArrayListRequest
        @return: DescribeDBInstanceIPArrayListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    async def describe_dbinstance_iparray_list_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        """
        You can call this operation to query the whitelists of IP addresses that are allowed to access an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstanceIPArrayListRequest
        @return: DescribeDBInstanceIPArrayListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_iparray_list_with_options_async(request, runtime)

    def describe_dbinstance_index_usage_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIndexUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse:
        """
        Appropriate indexes can accelerate database queries. You can call this operation to query the index usage of an AnalyticDB for PostgreSQL instance.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDBInstanceIndexUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceIndexUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIndexUsage',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_index_usage_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIndexUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse:
        """
        Appropriate indexes can accelerate database queries. You can call this operation to query the index usage of an AnalyticDB for PostgreSQL instance.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDBInstanceIndexUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceIndexUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceIndexUsage',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_index_usage(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIndexUsageRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse:
        """
        Appropriate indexes can accelerate database queries. You can call this operation to query the index usage of an AnalyticDB for PostgreSQL instance.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDBInstanceIndexUsageRequest
        @return: DescribeDBInstanceIndexUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_index_usage_with_options(request, runtime)

    async def describe_dbinstance_index_usage_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIndexUsageRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse:
        """
        Appropriate indexes can accelerate database queries. You can call this operation to query the index usage of an AnalyticDB for PostgreSQL instance.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDBInstanceIndexUsageRequest
        @return: DescribeDBInstanceIndexUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_index_usage_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_dbinstance_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_dbinstance_plans_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancePlansResponse:
        """
        You can call this operation to query the details of plans for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstancePlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancePlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_create_date):
            query['PlanCreateDate'] = request.plan_create_date
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePlans',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_plans_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancePlansResponse:
        """
        You can call this operation to query the details of plans for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstancePlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancePlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_create_date):
            query['PlanCreateDate'] = request.plan_create_date
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_schedule_type):
            query['PlanScheduleType'] = request.plan_schedule_type
        if not UtilClient.is_unset(request.plan_type):
            query['PlanType'] = request.plan_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstancePlans',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_plans(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePlansRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancePlansResponse:
        """
        You can call this operation to query the details of plans for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstancePlansRequest
        @return: DescribeDBInstancePlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_plans_with_options(request, runtime)

    async def describe_dbinstance_plans_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePlansRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancePlansResponse:
        """
        You can call this operation to query the details of plans for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstancePlansRequest
        @return: DescribeDBInstancePlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_plans_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSSL',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_dbinstance_support_max_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSupportMaxPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_support_max_performance_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceSupportMaxPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_support_max_performance(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_support_max_performance_with_options(request, runtime)

    async def describe_dbinstance_support_max_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceSupportMaxPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_support_max_performance_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        tmp_req: gpdb_20160503_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        """
        ##
        You can call this operation to query the instance types, network types, and states of AnalyticDB for PostgreSQL instances within a region.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.DescribeDBInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbinstance_categories):
            request.dbinstance_categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_categories, 'DBInstanceCategories', 'simple')
        if not UtilClient.is_unset(tmp_req.dbinstance_modes):
            request.dbinstance_modes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_modes, 'DBInstanceModes', 'simple')
        if not UtilClient.is_unset(tmp_req.dbinstance_statuses):
            request.dbinstance_statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_statuses, 'DBInstanceStatuses', 'simple')
        if not UtilClient.is_unset(tmp_req.instance_deploy_types):
            request.instance_deploy_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_deploy_types, 'InstanceDeployTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_categories_shrink):
            query['DBInstanceCategories'] = request.dbinstance_categories_shrink
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_modes_shrink):
            query['DBInstanceModes'] = request.dbinstance_modes_shrink
        if not UtilClient.is_unset(request.dbinstance_statuses_shrink):
            query['DBInstanceStatuses'] = request.dbinstance_statuses_shrink
        if not UtilClient.is_unset(request.instance_deploy_types_shrink):
            query['InstanceDeployTypes'] = request.instance_deploy_types_shrink
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        tmp_req: gpdb_20160503_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        """
        ##
        You can call this operation to query the instance types, network types, and states of AnalyticDB for PostgreSQL instances within a region.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param tmp_req: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.DescribeDBInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbinstance_categories):
            request.dbinstance_categories_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_categories, 'DBInstanceCategories', 'simple')
        if not UtilClient.is_unset(tmp_req.dbinstance_modes):
            request.dbinstance_modes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_modes, 'DBInstanceModes', 'simple')
        if not UtilClient.is_unset(tmp_req.dbinstance_statuses):
            request.dbinstance_statuses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_statuses, 'DBInstanceStatuses', 'simple')
        if not UtilClient.is_unset(tmp_req.instance_deploy_types):
            request.instance_deploy_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_deploy_types, 'InstanceDeployTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_categories_shrink):
            query['DBInstanceCategories'] = request.dbinstance_categories_shrink
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_modes_shrink):
            query['DBInstanceModes'] = request.dbinstance_modes_shrink
        if not UtilClient.is_unset(request.dbinstance_statuses_shrink):
            query['DBInstanceStatuses'] = request.dbinstance_statuses_shrink
        if not UtilClient.is_unset(request.instance_deploy_types_shrink):
            query['InstanceDeployTypes'] = request.instance_deploy_types_shrink
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: gpdb_20160503_models.DescribeDBInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        """
        ##
        You can call this operation to query the instance types, network types, and states of AnalyticDB for PostgreSQL instances within a region.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        """
        ##
        You can call this operation to query the instance types, network types, and states of AnalyticDB for PostgreSQL instances within a region.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbversion_infos_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBVersionInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBVersionInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBVersionInfos',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBVersionInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbversion_infos_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBVersionInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBVersionInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_mode):
            query['DBInstanceMode'] = request.dbinstance_mode
        if not UtilClient.is_unset(request.dbversion):
            query['DBVersion'] = request.dbversion
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBVersionInfos',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBVersionInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbversion_infos(
        self,
        request: gpdb_20160503_models.DescribeDBVersionInfosRequest,
    ) -> gpdb_20160503_models.DescribeDBVersionInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbversion_infos_with_options(request, runtime)

    async def describe_dbversion_infos_async(
        self,
        request: gpdb_20160503_models.DescribeDBVersionInfosRequest,
    ) -> gpdb_20160503_models.DescribeDBVersionInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbversion_infos_with_options_async(request, runtime)

    def describe_data_backups_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        """
        You can call this operation to query a list of backup sets and backup details only for instances in elastic storage mode.
        
        @param request: DescribeDataBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataBackups',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_backups_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        """
        You can call this operation to query a list of backup sets and backup details only for instances in elastic storage mode.
        
        @param request: DescribeDataBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not UtilClient.is_unset(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataBackups',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_backups(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        """
        You can call this operation to query a list of backup sets and backup details only for instances in elastic storage mode.
        
        @param request: DescribeDataBackupsRequest
        @return: DescribeDataBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_backups_with_options(request, runtime)

    async def describe_data_backups_async(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        """
        You can call this operation to query a list of backup sets and backup details only for instances in elastic storage mode.
        
        @param request: DescribeDataBackupsRequest
        @return: DescribeDataBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_backups_with_options_async(request, runtime)

    def describe_data_re_distribute_info_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataReDistributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataReDistributeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataReDistributeInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataReDistributeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_re_distribute_info_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDataReDistributeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataReDistributeInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataReDistributeInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataReDistributeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_re_distribute_info(
        self,
        request: gpdb_20160503_models.DescribeDataReDistributeInfoRequest,
    ) -> gpdb_20160503_models.DescribeDataReDistributeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_re_distribute_info_with_options(request, runtime)

    async def describe_data_re_distribute_info_async(
        self,
        request: gpdb_20160503_models.DescribeDataReDistributeInfoRequest,
    ) -> gpdb_20160503_models.DescribeDataReDistributeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_re_distribute_info_with_options_async(request, runtime)

    def describe_data_share_instances_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataShareInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataShareInstancesResponse:
        """
        Data sharing is supported only for instances in Serverless mode.
        
        @param request: DescribeDataShareInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataShareInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataShareInstances',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataShareInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_share_instances_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDataShareInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataShareInstancesResponse:
        """
        Data sharing is supported only for instances in Serverless mode.
        
        @param request: DescribeDataShareInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataShareInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataShareInstances',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataShareInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_share_instances(
        self,
        request: gpdb_20160503_models.DescribeDataShareInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDataShareInstancesResponse:
        """
        Data sharing is supported only for instances in Serverless mode.
        
        @param request: DescribeDataShareInstancesRequest
        @return: DescribeDataShareInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_share_instances_with_options(request, runtime)

    async def describe_data_share_instances_async(
        self,
        request: gpdb_20160503_models.DescribeDataShareInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDataShareInstancesResponse:
        """
        Data sharing is supported only for instances in Serverless mode.
        
        @param request: DescribeDataShareInstancesRequest
        @return: DescribeDataShareInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_share_instances_with_options_async(request, runtime)

    def describe_data_share_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataSharePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataSharePerformanceResponse:
        """
        You can call this operation to query the details of data sharing performance metrics for an AnalyticDB for PostgreSQL instance in Serverless mode, such as the number of shared topics and the amount of data shared.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDataSharePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSharePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataSharePerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataSharePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_share_performance_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDataSharePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataSharePerformanceResponse:
        """
        You can call this operation to query the details of data sharing performance metrics for an AnalyticDB for PostgreSQL instance in Serverless mode, such as the number of shared topics and the amount of data shared.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDataSharePerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataSharePerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataSharePerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataSharePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_share_performance(
        self,
        request: gpdb_20160503_models.DescribeDataSharePerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDataSharePerformanceResponse:
        """
        You can call this operation to query the details of data sharing performance metrics for an AnalyticDB for PostgreSQL instance in Serverless mode, such as the number of shared topics and the amount of data shared.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDataSharePerformanceRequest
        @return: DescribeDataSharePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_share_performance_with_options(request, runtime)

    async def describe_data_share_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDataSharePerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDataSharePerformanceResponse:
        """
        You can call this operation to query the details of data sharing performance metrics for an AnalyticDB for PostgreSQL instance in Serverless mode, such as the number of shared topics and the amount of data shared.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDataSharePerformanceRequest
        @return: DescribeDataSharePerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_share_performance_with_options_async(request, runtime)

    def describe_diagnosis_dimensions_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisDimensionsResponse:
        """
        To facilitate management, you can call this operation to query all databases and database accounts on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisDimensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisDimensions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_dimensions_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisDimensionsResponse:
        """
        To facilitate management, you can call this operation to query all databases and database accounts on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisDimensionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisDimensions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_dimensions(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisDimensionsRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisDimensionsResponse:
        """
        To facilitate management, you can call this operation to query all databases and database accounts on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @return: DescribeDiagnosisDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    async def describe_diagnosis_dimensions_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisDimensionsRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisDimensionsResponse:
        """
        To facilitate management, you can call this operation to query all databases and database accounts on an AnalyticDB for PostgreSQL instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisDimensionsRequest
        @return: DescribeDiagnosisDimensionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_dimensions_with_options_async(request, runtime)

    def describe_diagnosis_monitor_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        You can call this operation to query the details of query execution on an AnalyticDB for PostgreSQL instance in elastic storage mode within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisMonitorPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_monitor_performance_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        You can call this operation to query the details of query execution on an AnalyticDB for PostgreSQL instance in elastic storage mode within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisMonitorPerformance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_monitor_performance(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        You can call this operation to query the details of query execution on an AnalyticDB for PostgreSQL instance in elastic storage mode within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_monitor_performance_with_options(request, runtime)

    async def describe_diagnosis_monitor_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse:
        """
        You can call this operation to query the details of query execution on an AnalyticDB for PostgreSQL instance in elastic storage mode within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisMonitorPerformanceRequest
        @return: DescribeDiagnosisMonitorPerformanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_monitor_performance_with_options_async(request, runtime)

    def describe_diagnosis_records_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisRecordsResponse:
        """
        You can call this operation to query the details of SQL queries on an AnalyticDB for PostgreSQL instance within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_records_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisRecordsResponse:
        """
        You can call this operation to query the details of SQL queries on an AnalyticDB for PostgreSQL instance within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_records(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisRecordsRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisRecordsResponse:
        """
        You can call this operation to query the details of SQL queries on an AnalyticDB for PostgreSQL instance within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisRecordsRequest
        @return: DescribeDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    async def describe_diagnosis_records_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisRecordsRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisRecordsResponse:
        """
        You can call this operation to query the details of SQL queries on an AnalyticDB for PostgreSQL instance within a specified time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDiagnosisRecordsRequest
        @return: DescribeDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_records_with_options_async(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse:
        """
        You can call this operation to query the information about a query for an AnalyticDB for PostgreSQL instance, including the SQL statement, execution plan text, and execution plan tree.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.query_id):
            query['QueryID'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSQLInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_sqlinfo_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse:
        """
        You can call this operation to query the information about a query for an AnalyticDB for PostgreSQL instance, including the SQL statement, execution plan text, and execution plan tree.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosisSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.query_id):
            query['QueryID'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSQLInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_sqlinfo(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisSQLInfoRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse:
        """
        You can call this operation to query the information about a query for an AnalyticDB for PostgreSQL instance, including the SQL statement, execution plan text, and execution plan tree.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @return: DescribeDiagnosisSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    async def describe_diagnosis_sqlinfo_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisSQLInfoRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse:
        """
        You can call this operation to query the information about a query for an AnalyticDB for PostgreSQL instance, including the SQL statement, execution plan text, and execution plan tree.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDiagnosisSQLInfoRequest
        @return: DescribeDiagnosisSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_sqlinfo_with_options_async(request, runtime)

    def describe_document_with_options(
        self,
        request: gpdb_20160503_models.DescribeDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDocument',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_document_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDocumentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDocument',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_document(
        self,
        request: gpdb_20160503_models.DescribeDocumentRequest,
    ) -> gpdb_20160503_models.DescribeDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_document_with_options(request, runtime)

    async def describe_document_async(
        self,
        request: gpdb_20160503_models.DescribeDocumentRequest,
    ) -> gpdb_20160503_models.DescribeDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_document_with_options_async(request, runtime)

    def describe_download_records_with_options(
        self,
        request: gpdb_20160503_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDownloadRecordsResponse:
        """
        You must call the [DownloadDiagnosisRecords](~~447700~~) operation to download the query diagnostic information before you can call this operation to query the download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDownloadRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDownloadRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_records_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDownloadRecordsResponse:
        """
        You must call the [DownloadDiagnosisRecords](~~447700~~) operation to download the query diagnostic information before you can call this operation to query the download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDownloadRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDownloadRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_records(
        self,
        request: gpdb_20160503_models.DescribeDownloadRecordsRequest,
    ) -> gpdb_20160503_models.DescribeDownloadRecordsResponse:
        """
        You must call the [DownloadDiagnosisRecords](~~447700~~) operation to download the query diagnostic information before you can call this operation to query the download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDownloadRecordsRequest
        @return: DescribeDownloadRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    async def describe_download_records_async(
        self,
        request: gpdb_20160503_models.DescribeDownloadRecordsRequest,
    ) -> gpdb_20160503_models.DescribeDownloadRecordsResponse:
        """
        You must call the [DownloadDiagnosisRecords](~~447700~~) operation to download the query diagnostic information before you can call this operation to query the download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For information about how to view and update the minor version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        
        @param request: DescribeDownloadRecordsRequest
        @return: DescribeDownloadRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_records_with_options_async(request, runtime)

    def describe_download_sqllogs_with_options(
        self,
        request: gpdb_20160503_models.DescribeDownloadSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDownloadSQLLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadSQLLogs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDownloadSQLLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_sqllogs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDownloadSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDownloadSQLLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadSQLLogs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDownloadSQLLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_sqllogs(
        self,
        request: gpdb_20160503_models.DescribeDownloadSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeDownloadSQLLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_download_sqllogs_with_options(request, runtime)

    async def describe_download_sqllogs_async(
        self,
        request: gpdb_20160503_models.DescribeDownloadSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeDownloadSQLLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_sqllogs_with_options_async(request, runtime)

    def describe_health_status_with_options(
        self,
        request: gpdb_20160503_models.DescribeHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeHealthStatusResponse:
        """
        This operation is called to query the health status of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode and its coordinator and compute nodes.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthStatus',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_health_status_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeHealthStatusResponse:
        """
        This operation is called to query the health status of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode and its coordinator and compute nodes.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthStatus',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_health_status(
        self,
        request: gpdb_20160503_models.DescribeHealthStatusRequest,
    ) -> gpdb_20160503_models.DescribeHealthStatusResponse:
        """
        This operation is called to query the health status of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode and its coordinator and compute nodes.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeHealthStatusRequest
        @return: DescribeHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    async def describe_health_status_async(
        self,
        request: gpdb_20160503_models.DescribeHealthStatusRequest,
    ) -> gpdb_20160503_models.DescribeHealthStatusResponse:
        """
        This operation is called to query the health status of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode and its coordinator and compute nodes.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeHealthStatusRequest
        @return: DescribeHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_status_with_options_async(request, runtime)

    def describe_imvinfos_with_options(
        self,
        request: gpdb_20160503_models.DescribeIMVInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeIMVInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.mvname):
            query['MVName'] = request.mvname
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIMVInfos',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeIMVInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imvinfos_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeIMVInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeIMVInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.mvname):
            query['MVName'] = request.mvname
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIMVInfos',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeIMVInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imvinfos(
        self,
        request: gpdb_20160503_models.DescribeIMVInfosRequest,
    ) -> gpdb_20160503_models.DescribeIMVInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_imvinfos_with_options(request, runtime)

    async def describe_imvinfos_async(
        self,
        request: gpdb_20160503_models.DescribeIMVInfosRequest,
    ) -> gpdb_20160503_models.DescribeIMVInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_imvinfos_with_options_async(request, runtime)

    def describe_log_backups_with_options(
        self,
        request: gpdb_20160503_models.DescribeLogBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeLogBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogBackups',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeLogBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_backups_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeLogBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeLogBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogBackups',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeLogBackupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModifyParameterLog',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeModifyParameterLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_modify_parameter_log_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeModifyParameterLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeModifyParameterLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModifyParameterLog',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeModifyParameterLogResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_namespace_with_options(
        self,
        request: gpdb_20160503_models.DescribeNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace(
        self,
        request: gpdb_20160503_models.DescribeNamespaceRequest,
    ) -> gpdb_20160503_models.DescribeNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_namespace_with_options(request, runtime)

    async def describe_namespace_async(
        self,
        request: gpdb_20160503_models.DescribeNamespaceRequest,
    ) -> gpdb_20160503_models.DescribeNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_namespace_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        """
        This operation can be called to query the details of parameters in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        """
        This operation can be called to query the details of parameters in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParameters',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        """
        This operation can be called to query the details of parameters in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        """
        This operation can be called to query the details of parameters in an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeParametersRequest
        @return: DescribeParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_rds_vswitchs_with_options(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        """
        When you create AnalyticDB for PostgreSQL instances, you can call this operation to query the details of vSwitches within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVSwitchsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVSwitchsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVSwitchs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVSwitchsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vswitchs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        """
        When you create AnalyticDB for PostgreSQL instances, you can call this operation to query the details of vSwitches within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVSwitchsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVSwitchsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVSwitchs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVSwitchsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vswitchs(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        """
        When you create AnalyticDB for PostgreSQL instances, you can call this operation to query the details of vSwitches within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVSwitchsRequest
        @return: DescribeRdsVSwitchsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vswitchs_with_options(request, runtime)

    async def describe_rds_vswitchs_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        """
        When you create AnalyticDB for PostgreSQL instances, you can call this operation to query the details of vSwitches within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVSwitchsRequest
        @return: DescribeRdsVSwitchsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vswitchs_with_options_async(request, runtime)

    def describe_rds_vpcs_with_options(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available VPCs within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVpcsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVpcs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vpcs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available VPCs within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdsVpcsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsVpcs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vpcs(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available VPCs within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVpcsRequest
        @return: DescribeRdsVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpcs_with_options(request, runtime)

    async def describe_rds_vpcs_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        """
        When you create an AnalyticDB for PostgreSQL instance, you can call this operation to query the available VPCs within a specified region or zone.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRdsVpcsRequest
        @return: DescribeRdsVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vpcs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        """
        Before you create an AnalyticDB for PostgreSQL instance, you must call this operation to query available regions and zones.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        """
        Before you create an AnalyticDB for PostgreSQL instance, you must call this operation to query available regions and zones.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        """
        Before you create an AnalyticDB for PostgreSQL instance, you must call this operation to query available regions and zones.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        """
        Before you create an AnalyticDB for PostgreSQL instance, you must call this operation to query available regions and zones.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_sqllog_count_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        """
        This operation is not available for instances in reserved storage mode.
        
        @param request: DescribeSQLLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogCount',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_count_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        """
        This operation is not available for instances in reserved storage mode.
        
        @param request: DescribeSQLLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogCount',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllog_count(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        """
        This operation is not available for instances in reserved storage mode.
        
        @param request: DescribeSQLLogCountRequest
        @return: DescribeSQLLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_count_with_options(request, runtime)

    async def describe_sqllog_count_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        """
        This operation is not available for instances in reserved storage mode.
        
        @param request: DescribeSQLLogCountRequest
        @return: DescribeSQLLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_count_with_options_async(request, runtime)

    def describe_sqllogs_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        """
        > This operation is no longer used. To query SQL execution logs, call the [DescribeSQLLogsV2](~~453722~~) operation.
        
        @param request: DescribeSQLLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllogs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        """
        > This operation is no longer used. To query SQL execution logs, call the [DescribeSQLLogsV2](~~453722~~) operation.
        
        @param request: DescribeSQLLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogs',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllogs(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        """
        > This operation is no longer used. To query SQL execution logs, call the [DescribeSQLLogsV2](~~453722~~) operation.
        
        @param request: DescribeSQLLogsRequest
        @return: DescribeSQLLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllogs_with_options(request, runtime)

    async def describe_sqllogs_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        """
        > This operation is no longer used. To query SQL execution logs, call the [DescribeSQLLogsV2](~~453722~~) operation.
        
        @param request: DescribeSQLLogsRequest
        @return: DescribeSQLLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllogs_with_options_async(request, runtime)

    def describe_sqllogs_v2with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsV2Response:
        """
        You can call this operation to query SQL logs of an AnalyticDB for PostgreSQL instance within a specific time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSQLLogsV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLLogsV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogsV2',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllogs_v2with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsV2Response:
        """
        You can call this operation to query SQL logs of an AnalyticDB for PostgreSQL instance within a specific time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSQLLogsV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSQLLogsV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogsV2',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqllogs_v2(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsV2Request,
    ) -> gpdb_20160503_models.DescribeSQLLogsV2Response:
        """
        You can call this operation to query SQL logs of an AnalyticDB for PostgreSQL instance within a specific time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSQLLogsV2Request
        @return: DescribeSQLLogsV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllogs_v2with_options(request, runtime)

    async def describe_sqllogs_v2_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsV2Request,
    ) -> gpdb_20160503_models.DescribeSQLLogsV2Response:
        """
        You can call this operation to query SQL logs of an AnalyticDB for PostgreSQL instance within a specific time range.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSQLLogsV2Request
        @return: DescribeSQLLogsV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllogs_v2with_options_async(request, runtime)

    def describe_sample_data_with_options(
        self,
        request: gpdb_20160503_models.DescribeSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSampleDataResponse:
        """
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSampleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sample_data_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSampleDataResponse:
        """
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSampleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sample_data(
        self,
        request: gpdb_20160503_models.DescribeSampleDataRequest,
    ) -> gpdb_20160503_models.DescribeSampleDataResponse:
        """
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSampleDataRequest
        @return: DescribeSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_data_with_options(request, runtime)

    async def describe_sample_data_async(
        self,
        request: gpdb_20160503_models.DescribeSampleDataRequest,
    ) -> gpdb_20160503_models.DescribeSampleDataResponse:
        """
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeSampleDataRequest
        @return: DescribeSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sample_data_with_options_async(request, runtime)

    def describe_support_features_with_options(
        self,
        request: gpdb_20160503_models.DescribeSupportFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSupportFeaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportFeatures',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSupportFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_support_features_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSupportFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSupportFeaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportFeatures',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSupportFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_support_features(
        self,
        request: gpdb_20160503_models.DescribeSupportFeaturesRequest,
    ) -> gpdb_20160503_models.DescribeSupportFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_support_features_with_options(request, runtime)

    async def describe_support_features_async(
        self,
        request: gpdb_20160503_models.DescribeSupportFeaturesRequest,
    ) -> gpdb_20160503_models.DescribeSupportFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_support_features_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: gpdb_20160503_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeUserEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeUserEncryptionKeyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserEncryptionKeyList',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeUserEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_waiting_sqlinfo_with_options(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeWaitingSQLInfoResponse:
        """
        You can call this operation to query the details of a lock-waiting query only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWaitingSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.pid):
            query['PID'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingSQLInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeWaitingSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waiting_sqlinfo_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeWaitingSQLInfoResponse:
        """
        You can call this operation to query the details of a lock-waiting query only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWaitingSQLInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.pid):
            query['PID'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingSQLInfo',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeWaitingSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waiting_sqlinfo(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLInfoRequest,
    ) -> gpdb_20160503_models.DescribeWaitingSQLInfoResponse:
        """
        You can call this operation to query the details of a lock-waiting query only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLInfoRequest
        @return: DescribeWaitingSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_waiting_sqlinfo_with_options(request, runtime)

    async def describe_waiting_sqlinfo_async(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLInfoRequest,
    ) -> gpdb_20160503_models.DescribeWaitingSQLInfoResponse:
        """
        You can call this operation to query the details of a lock-waiting query only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLInfoRequest
        @return: DescribeWaitingSQLInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_waiting_sqlinfo_with_options_async(request, runtime)

    def describe_waiting_sqlrecords_with_options(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeWaitingSQLRecordsResponse:
        """
        You can call this operation to query the lock diagnostics records only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWaitingSQLRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingSQLRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeWaitingSQLRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waiting_sqlrecords_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeWaitingSQLRecordsResponse:
        """
        You can call this operation to query the lock diagnostics records only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWaitingSQLRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWaitingSQLRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeWaitingSQLRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waiting_sqlrecords(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLRecordsRequest,
    ) -> gpdb_20160503_models.DescribeWaitingSQLRecordsResponse:
        """
        You can call this operation to query the lock diagnostics records only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLRecordsRequest
        @return: DescribeWaitingSQLRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_waiting_sqlrecords_with_options(request, runtime)

    async def describe_waiting_sqlrecords_async(
        self,
        request: gpdb_20160503_models.DescribeWaitingSQLRecordsRequest,
    ) -> gpdb_20160503_models.DescribeWaitingSQLRecordsResponse:
        """
        You can call this operation to query the lock diagnostics records only for an AnalyticDB for PostgreSQL V6.0 instance in elastic storage mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeWaitingSQLRecordsRequest
        @return: DescribeWaitingSQLRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_waiting_sqlrecords_with_options_async(request, runtime)

    def download_diagnosis_records_with_options(
        self,
        request: gpdb_20160503_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DownloadDiagnosisRecordsResponse:
        """
        You can call this operation to download the query diagnostic information of an AnalyticDB for PostgreSQL instance. After the download is complete, you can call the [DescribeDownloadRecords](~~447712~~) operation to query download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DownloadDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDiagnosisRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DownloadDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_diagnosis_records_with_options_async(
        self,
        request: gpdb_20160503_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DownloadDiagnosisRecordsResponse:
        """
        You can call this operation to download the query diagnostic information of an AnalyticDB for PostgreSQL instance. After the download is complete, you can call the [DescribeDownloadRecords](~~447712~~) operation to query download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DownloadDiagnosisRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadDiagnosisRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDiagnosisRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DownloadDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_diagnosis_records(
        self,
        request: gpdb_20160503_models.DownloadDiagnosisRecordsRequest,
    ) -> gpdb_20160503_models.DownloadDiagnosisRecordsResponse:
        """
        You can call this operation to download the query diagnostic information of an AnalyticDB for PostgreSQL instance. After the download is complete, you can call the [DescribeDownloadRecords](~~447712~~) operation to query download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DownloadDiagnosisRecordsRequest
        @return: DownloadDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    async def download_diagnosis_records_async(
        self,
        request: gpdb_20160503_models.DownloadDiagnosisRecordsRequest,
    ) -> gpdb_20160503_models.DownloadDiagnosisRecordsResponse:
        """
        You can call this operation to download the query diagnostic information of an AnalyticDB for PostgreSQL instance. After the download is complete, you can call the [DescribeDownloadRecords](~~447712~~) operation to query download records and download URLs.
        This operation is available only for instances of V6.3.10.1 or later in elastic storage mode. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DownloadDiagnosisRecordsRequest
        @return: DownloadDiagnosisRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_diagnosis_records_with_options_async(request, runtime)

    def download_sqllogs_records_with_options(
        self,
        request: gpdb_20160503_models.DownloadSQLLogsRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DownloadSQLLogsRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadSQLLogsRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DownloadSQLLogsRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_sqllogs_records_with_options_async(
        self,
        request: gpdb_20160503_models.DownloadSQLLogsRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DownloadSQLLogsRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_cost):
            query['ExecuteCost'] = request.execute_cost
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.operation_class):
            query['OperationClass'] = request.operation_class
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIP'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadSQLLogsRecords',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DownloadSQLLogsRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_sqllogs_records(
        self,
        request: gpdb_20160503_models.DownloadSQLLogsRecordsRequest,
    ) -> gpdb_20160503_models.DownloadSQLLogsRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_sqllogs_records_with_options(request, runtime)

    async def download_sqllogs_records_async(
        self,
        request: gpdb_20160503_models.DownloadSQLLogsRecordsRequest,
    ) -> gpdb_20160503_models.DownloadSQLLogsRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_sqllogs_records_with_options_async(request, runtime)

    def grant_collection_with_options(
        self,
        request: gpdb_20160503_models.GrantCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.GrantCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.grant_to_namespace):
            query['GrantToNamespace'] = request.grant_to_namespace
        if not UtilClient.is_unset(request.grant_type):
            query['GrantType'] = request.grant_type
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.GrantCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_collection_with_options_async(
        self,
        request: gpdb_20160503_models.GrantCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.GrantCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.grant_to_namespace):
            query['GrantToNamespace'] = request.grant_to_namespace
        if not UtilClient.is_unset(request.grant_type):
            query['GrantType'] = request.grant_type
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantCollection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.GrantCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_collection(
        self,
        request: gpdb_20160503_models.GrantCollectionRequest,
    ) -> gpdb_20160503_models.GrantCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_collection_with_options(request, runtime)

    async def grant_collection_async(
        self,
        request: gpdb_20160503_models.GrantCollectionRequest,
    ) -> gpdb_20160503_models.GrantCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_collection_with_options_async(request, runtime)

    def handle_active_sqlrecord_with_options(
        self,
        request: gpdb_20160503_models.HandleActiveSQLRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.HandleActiveSQLRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleActiveSQLRecord',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.HandleActiveSQLRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_active_sqlrecord_with_options_async(
        self,
        request: gpdb_20160503_models.HandleActiveSQLRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.HandleActiveSQLRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleActiveSQLRecord',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.HandleActiveSQLRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_active_sqlrecord(
        self,
        request: gpdb_20160503_models.HandleActiveSQLRecordRequest,
    ) -> gpdb_20160503_models.HandleActiveSQLRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.handle_active_sqlrecord_with_options(request, runtime)

    async def handle_active_sqlrecord_async(
        self,
        request: gpdb_20160503_models.HandleActiveSQLRecordRequest,
    ) -> gpdb_20160503_models.HandleActiveSQLRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.handle_active_sqlrecord_with_options_async(request, runtime)

    def init_vector_database_with_options(
        self,
        request: gpdb_20160503_models.InitVectorDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.InitVectorDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitVectorDatabase',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.InitVectorDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_vector_database_with_options_async(
        self,
        request: gpdb_20160503_models.InitVectorDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.InitVectorDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitVectorDatabase',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.InitVectorDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_vector_database(
        self,
        request: gpdb_20160503_models.InitVectorDatabaseRequest,
    ) -> gpdb_20160503_models.InitVectorDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_vector_database_with_options(request, runtime)

    async def init_vector_database_async(
        self,
        request: gpdb_20160503_models.InitVectorDatabaseRequest,
    ) -> gpdb_20160503_models.InitVectorDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_vector_database_with_options_async(request, runtime)

    def list_collections_with_options(
        self,
        request: gpdb_20160503_models.ListCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListCollectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollections',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_collections_with_options_async(
        self,
        request: gpdb_20160503_models.ListCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListCollectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollections',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_collections(
        self,
        request: gpdb_20160503_models.ListCollectionsRequest,
    ) -> gpdb_20160503_models.ListCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_collections_with_options(request, runtime)

    async def list_collections_async(
        self,
        request: gpdb_20160503_models.ListCollectionsRequest,
    ) -> gpdb_20160503_models.ListCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_collections_with_options_async(request, runtime)

    def list_document_collections_with_options(
        self,
        request: gpdb_20160503_models.ListDocumentCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListDocumentCollectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDocumentCollections',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListDocumentCollectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_document_collections_with_options_async(
        self,
        request: gpdb_20160503_models.ListDocumentCollectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListDocumentCollectionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDocumentCollections',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListDocumentCollectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_document_collections(
        self,
        request: gpdb_20160503_models.ListDocumentCollectionsRequest,
    ) -> gpdb_20160503_models.ListDocumentCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_document_collections_with_options(request, runtime)

    async def list_document_collections_async(
        self,
        request: gpdb_20160503_models.ListDocumentCollectionsRequest,
    ) -> gpdb_20160503_models.ListDocumentCollectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_document_collections_with_options_async(request, runtime)

    def list_documents_with_options(
        self,
        request: gpdb_20160503_models.ListDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListDocumentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDocuments',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_documents_with_options_async(
        self,
        request: gpdb_20160503_models.ListDocumentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListDocumentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDocuments',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_documents(
        self,
        request: gpdb_20160503_models.ListDocumentsRequest,
    ) -> gpdb_20160503_models.ListDocumentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_documents_with_options(request, runtime)

    async def list_documents_async(
        self,
        request: gpdb_20160503_models.ListDocumentsRequest,
    ) -> gpdb_20160503_models.ListDocumentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_documents_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: gpdb_20160503_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListNamespacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: gpdb_20160503_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListNamespacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.manager_account):
            query['ManagerAccount'] = request.manager_account
        if not UtilClient.is_unset(request.manager_account_password):
            query['ManagerAccountPassword'] = request.manager_account_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: gpdb_20160503_models.ListNamespacesRequest,
    ) -> gpdb_20160503_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: gpdb_20160503_models.ListNamespacesRequest,
    ) -> gpdb_20160503_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: gpdb_20160503_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListTagResourcesResponse:
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
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: gpdb_20160503_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListTagResourcesResponse:
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
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.enable_recovery_point):
            query['EnableRecoveryPoint'] = request.enable_recovery_point
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.recovery_point_period):
            query['RecoveryPointPeriod'] = request.recovery_point_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.enable_recovery_point):
            query['EnableRecoveryPoint'] = request.enable_recovery_point
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.recovery_point_period):
            query['RecoveryPointPeriod'] = request.recovery_point_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_dbinstance_config_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_config_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.idle_time):
            query['IdleTime'] = request.idle_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.serverless_resource):
            query['ServerlessResource'] = request.serverless_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_config(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConfigRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    async def modify_dbinstance_config_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConfigRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_config_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        To make it easy to identify AnalyticDB for PostgreSQL instances, you can call this operation to modify the description of instances.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceDescriptionResponse:
        """
        To make it easy to identify AnalyticDB for PostgreSQL instances, you can call this operation to modify the description of instances.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceDescription',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceDescriptionRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceDescriptionResponse:
        """
        To make it easy to identify AnalyticDB for PostgreSQL instances, you can call this operation to modify the description of instances.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @return: ModifyDBInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceDescriptionRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceDescriptionResponse:
        """
        To make it easy to identify AnalyticDB for PostgreSQL instances, you can call this operation to modify the description of instances.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceDescriptionRequest
        @return: ModifyDBInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        """
        The system maintains AnalyticDB for PostgreSQL instances during the maintenance window that you specify. We recommend that you set the maintenance window to off-peak hours to minimize the impact on your business.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        """
        The system maintains AnalyticDB for PostgreSQL instances during the maintenance window that you specify. We recommend that you set the maintenance window to off-peak hours to minimize the impact on your business.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceMaintainTime',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        """
        The system maintains AnalyticDB for PostgreSQL instances during the maintenance window that you specify. We recommend that you set the maintenance window to off-peak hours to minimize the impact on your business.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        """
        The system maintains AnalyticDB for PostgreSQL instances during the maintenance window that you specify. We recommend that you set the maintenance window to off-peak hours to minimize the impact on your business.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyDBInstanceMaintainTimeRequest
        @return: ModifyDBInstanceMaintainTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_resource_group_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse:
        """
        Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475~~)
        
        @param request: ModifyDBInstanceResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='ModifyDBInstanceResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_resource_group_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse:
        """
        Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475~~)
        
        @param request: ModifyDBInstanceResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='ModifyDBInstanceResourceGroup',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_resource_group(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceResourceGroupRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse:
        """
        Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475~~)
        
        @param request: ModifyDBInstanceResourceGroupRequest
        @return: ModifyDBInstanceResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_resource_group_with_options(request, runtime)

    async def modify_dbinstance_resource_group_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceResourceGroupRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse:
        """
        Resource Management allows you to build an organizational structure for resources based on your business requirements. You can use resource directories, folders, accounts, and resource groups to hierarchically organize and manage resources. For more information, see [What is Resource Management?](~~94475~~)
        
        @param request: ModifyDBInstanceResourceGroupRequest
        @return: ModifyDBInstanceResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_resource_group_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceSSL',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_master_spec_with_options(
        self,
        request: gpdb_20160503_models.ModifyMasterSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyMasterSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMasterSpec',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyMasterSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_master_spec_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyMasterSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyMasterSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.master_cu):
            query['MasterCU'] = request.master_cu
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMasterSpec',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyMasterSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_master_spec(
        self,
        request: gpdb_20160503_models.ModifyMasterSpecRequest,
    ) -> gpdb_20160503_models.ModifyMasterSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_master_spec_with_options(request, runtime)

    async def modify_master_spec_async(
        self,
        request: gpdb_20160503_models.ModifyMasterSpecRequest,
    ) -> gpdb_20160503_models.ModifyMasterSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_master_spec_with_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        """
        This operation can be called to modify parameters of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.force_restart_instance):
            query['ForceRestartInstance'] = request.force_restart_instance
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameters_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        """
        This operation can be called to modify parameters of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParametersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.force_restart_instance):
            query['ForceRestartInstance'] = request.force_restart_instance
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParameters',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameters(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        """
        This operation can be called to modify parameters of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyParametersRequest
        @return: ModifyParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        """
        This operation can be called to modify parameters of an AnalyticDB for PostgreSQL instance in elastic storage mode or Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyParametersRequest
        @return: ModifyParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_sqlcollector_policy_with_options(
        self,
        request: gpdb_20160503_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.sqlcollector_status):
            query['SQLCollectorStatus'] = request.sqlcollector_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sqlcollector_policy_with_options_async(
        self,
        request: gpdb_20160503_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.sqlcollector_status):
            query['SQLCollectorStatus'] = request.sqlcollector_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySQLCollectorPolicy',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySQLCollectorPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_security_ips_with_options(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        """
        To ensure the security and stability of AnalyticDB for PostgreSQL instances, the system denies all external IP addresses to access AnalyticDB for PostgreSQL instances by default. Before you can use an AnalyticDB for PostgreSQL instance, you must add the IP address or CIDR block of your client to the IP address whitelist of the instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        """
        To ensure the security and stability of AnalyticDB for PostgreSQL instances, the system denies all external IP addresses to access AnalyticDB for PostgreSQL instances by default. Before you can use an AnalyticDB for PostgreSQL instance, you must add the IP address or CIDR block of your client to the IP address whitelist of the instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySecurityIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIps',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        """
        To ensure the security and stability of AnalyticDB for PostgreSQL instances, the system denies all external IP addresses to access AnalyticDB for PostgreSQL instances by default. Before you can use an AnalyticDB for PostgreSQL instance, you must add the IP address or CIDR block of your client to the IP address whitelist of the instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        """
        To ensure the security and stability of AnalyticDB for PostgreSQL instances, the system denies all external IP addresses to access AnalyticDB for PostgreSQL instances by default. Before you can use an AnalyticDB for PostgreSQL instance, you must add the IP address or CIDR block of your client to the IP address whitelist of the instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifySecurityIpsRequest
        @return: ModifySecurityIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_vector_configuration_with_options(
        self,
        request: gpdb_20160503_models.ModifyVectorConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyVectorConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVectorConfiguration',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyVectorConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vector_configuration_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyVectorConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyVectorConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.vector_configuration_status):
            query['VectorConfigurationStatus'] = request.vector_configuration_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVectorConfiguration',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyVectorConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vector_configuration(
        self,
        request: gpdb_20160503_models.ModifyVectorConfigurationRequest,
    ) -> gpdb_20160503_models.ModifyVectorConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vector_configuration_with_options(request, runtime)

    async def modify_vector_configuration_async(
        self,
        request: gpdb_20160503_models.ModifyVectorConfigurationRequest,
    ) -> gpdb_20160503_models.ModifyVectorConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vector_configuration_with_options_async(request, runtime)

    def pause_instance_with_options(
        self,
        request: gpdb_20160503_models.PauseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.PauseInstanceResponse:
        """
        You can call this operation to pause an AnalyticDB for PostgreSQL instance that is in the *Running** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PauseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.PauseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_instance_with_options_async(
        self,
        request: gpdb_20160503_models.PauseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.PauseInstanceResponse:
        """
        You can call this operation to pause an AnalyticDB for PostgreSQL instance that is in the *Running** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PauseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.PauseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_instance(
        self,
        request: gpdb_20160503_models.PauseInstanceRequest,
    ) -> gpdb_20160503_models.PauseInstanceResponse:
        """
        You can call this operation to pause an AnalyticDB for PostgreSQL instance that is in the *Running** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PauseInstanceRequest
        @return: PauseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_instance_with_options(request, runtime)

    async def pause_instance_async(
        self,
        request: gpdb_20160503_models.PauseInstanceRequest,
    ) -> gpdb_20160503_models.PauseInstanceResponse:
        """
        You can call this operation to pause an AnalyticDB for PostgreSQL instance that is in the *Running** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PauseInstanceRequest
        @return: PauseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pause_instance_with_options_async(request, runtime)

    def query_collection_data_with_options(
        self,
        tmp_req: gpdb_20160503_models.QueryCollectionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.QueryCollectionDataResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.QueryCollectionDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vector):
            request.vector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vector, 'Vector', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_values):
            query['IncludeValues'] = request.include_values
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.vector_shrink):
            query['Vector'] = request.vector_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.QueryCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_collection_data_with_options_async(
        self,
        tmp_req: gpdb_20160503_models.QueryCollectionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.QueryCollectionDataResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.QueryCollectionDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vector):
            request.vector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vector, 'Vector', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_values):
            query['IncludeValues'] = request.include_values
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.vector_shrink):
            query['Vector'] = request.vector_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.QueryCollectionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_collection_data(
        self,
        request: gpdb_20160503_models.QueryCollectionDataRequest,
    ) -> gpdb_20160503_models.QueryCollectionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_collection_data_with_options(request, runtime)

    async def query_collection_data_async(
        self,
        request: gpdb_20160503_models.QueryCollectionDataRequest,
    ) -> gpdb_20160503_models.QueryCollectionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_collection_data_with_options_async(request, runtime)

    def query_content_with_options(
        self,
        request: gpdb_20160503_models.QueryContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.QueryContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.use_full_text_retrieval):
            query['UseFullTextRetrieval'] = request.use_full_text_retrieval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContent',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.QueryContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_content_with_options_async(
        self,
        request: gpdb_20160503_models.QueryContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.QueryContentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_k):
            query['TopK'] = request.top_k
        if not UtilClient.is_unset(request.use_full_text_retrieval):
            query['UseFullTextRetrieval'] = request.use_full_text_retrieval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryContent',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.QueryContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_content(
        self,
        request: gpdb_20160503_models.QueryContentRequest,
    ) -> gpdb_20160503_models.QueryContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_content_with_options(request, runtime)

    async def query_content_async(
        self,
        request: gpdb_20160503_models.QueryContentRequest,
    ) -> gpdb_20160503_models.QueryContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_content_with_options_async(request, runtime)

    def rebalance_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.RebalanceDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.RebalanceDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RebalanceDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebalance_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.RebalanceDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.RebalanceDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RebalanceDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebalance_dbinstance(
        self,
        request: gpdb_20160503_models.RebalanceDBInstanceRequest,
    ) -> gpdb_20160503_models.RebalanceDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebalance_dbinstance_with_options(request, runtime)

    async def rebalance_dbinstance_async(
        self,
        request: gpdb_20160503_models.RebalanceDBInstanceRequest,
    ) -> gpdb_20160503_models.RebalanceDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebalance_dbinstance_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: gpdb_20160503_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: gpdb_20160503_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: gpdb_20160503_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
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

    def reset_imvmonitor_data_with_options(
        self,
        request: gpdb_20160503_models.ResetIMVMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResetIMVMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetIMVMonitorData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetIMVMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_imvmonitor_data_with_options_async(
        self,
        request: gpdb_20160503_models.ResetIMVMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResetIMVMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetIMVMonitorData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetIMVMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_imvmonitor_data(
        self,
        request: gpdb_20160503_models.ResetIMVMonitorDataRequest,
    ) -> gpdb_20160503_models.ResetIMVMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_imvmonitor_data_with_options(request, runtime)

    async def reset_imvmonitor_data_async(
        self,
        request: gpdb_20160503_models.ResetIMVMonitorDataRequest,
    ) -> gpdb_20160503_models.ResetIMVMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_imvmonitor_data_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        """
        A restart takes about 3 to 30 minutes. During the restart, services are unavailable. We recommend that you restart the instance during off-peak hours. After the instance is restarted and enters the running state, you can access the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        """
        A restart takes about 3 to 30 minutes. During the restart, services are unavailable. We recommend that you restart the instance during off-peak hours. After the instance is restarted and enters the running state, you can access the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        """
        A restart takes about 3 to 30 minutes. During the restart, services are unavailable. We recommend that you restart the instance during off-peak hours. After the instance is restarted and enters the running state, you can access the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        """
        A restart takes about 3 to 30 minutes. During the restart, services are unavailable. We recommend that you restart the instance during off-peak hours. After the instance is restarted and enters the running state, you can access the instance.
        ## Limit
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered and may affect your business. We recommend that you take note of the limit when you call this operation.
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def resume_instance_with_options(
        self,
        request: gpdb_20160503_models.ResumeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResumeInstanceResponse:
        """
        You can call this operation to resume an AnalyticDB for PostgreSQL instance that is in the *Paused** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResumeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        request: gpdb_20160503_models.ResumeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResumeInstanceResponse:
        """
        You can call this operation to resume an AnalyticDB for PostgreSQL instance that is in the *Paused** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResumeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResumeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance(
        self,
        request: gpdb_20160503_models.ResumeInstanceRequest,
    ) -> gpdb_20160503_models.ResumeInstanceResponse:
        """
        You can call this operation to resume an AnalyticDB for PostgreSQL instance that is in the *Paused** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResumeInstanceRequest
        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    async def resume_instance_async(
        self,
        request: gpdb_20160503_models.ResumeInstanceRequest,
    ) -> gpdb_20160503_models.ResumeInstanceResponse:
        """
        You can call this operation to resume an AnalyticDB for PostgreSQL instance that is in the *Paused** state.
        This operation is available only for AnalyticDB for PostgreSQL instances in Serverless mode that run V1.0.2.1 or later. For more information about how to view and update the minor engine version of an instance, see [View the minor engine version](~~277424~~) and [Update the minor engine version](~~139271~~).
        >  Before you call this operation, make sure that you are familiar with the billing methods and pricing of AnalyticDB for PostgreSQL instances. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResumeInstanceRequest
        @return: ResumeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_instance_with_options_async(request, runtime)

    def set_dbinstance_plan_status_with_options(
        self,
        request: gpdb_20160503_models.SetDBInstancePlanStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SetDBInstancePlanStatusResponse:
        """
        You can call this operation to enable or disable a specified plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SetDBInstancePlanStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDBInstancePlanStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_status):
            query['PlanStatus'] = request.plan_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDBInstancePlanStatus',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SetDBInstancePlanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dbinstance_plan_status_with_options_async(
        self,
        request: gpdb_20160503_models.SetDBInstancePlanStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SetDBInstancePlanStatusResponse:
        """
        You can call this operation to enable or disable a specified plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SetDBInstancePlanStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDBInstancePlanStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_status):
            query['PlanStatus'] = request.plan_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDBInstancePlanStatus',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SetDBInstancePlanStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dbinstance_plan_status(
        self,
        request: gpdb_20160503_models.SetDBInstancePlanStatusRequest,
    ) -> gpdb_20160503_models.SetDBInstancePlanStatusResponse:
        """
        You can call this operation to enable or disable a specified plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SetDBInstancePlanStatusRequest
        @return: SetDBInstancePlanStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dbinstance_plan_status_with_options(request, runtime)

    async def set_dbinstance_plan_status_async(
        self,
        request: gpdb_20160503_models.SetDBInstancePlanStatusRequest,
    ) -> gpdb_20160503_models.SetDBInstancePlanStatusResponse:
        """
        You can call this operation to enable or disable a specified plan. The plan management feature is supported only for AnalyticDB for PostgreSQL instances in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: SetDBInstancePlanStatusRequest
        @return: SetDBInstancePlanStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dbinstance_plan_status_with_options_async(request, runtime)

    def set_data_share_instance_with_options(
        self,
        tmp_req: gpdb_20160503_models.SetDataShareInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SetDataShareInstanceResponse:
        """
        This operation is called to enable or disable data sharing for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param tmp_req: SetDataShareInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataShareInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.SetDataShareInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataShareInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SetDataShareInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_data_share_instance_with_options_async(
        self,
        tmp_req: gpdb_20160503_models.SetDataShareInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SetDataShareInstanceResponse:
        """
        This operation is called to enable or disable data sharing for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param tmp_req: SetDataShareInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDataShareInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.SetDataShareInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDataShareInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SetDataShareInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_data_share_instance(
        self,
        request: gpdb_20160503_models.SetDataShareInstanceRequest,
    ) -> gpdb_20160503_models.SetDataShareInstanceResponse:
        """
        This operation is called to enable or disable data sharing for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: SetDataShareInstanceRequest
        @return: SetDataShareInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_data_share_instance_with_options(request, runtime)

    async def set_data_share_instance_async(
        self,
        request: gpdb_20160503_models.SetDataShareInstanceRequest,
    ) -> gpdb_20160503_models.SetDataShareInstanceResponse:
        """
        This operation is called to enable or disable data sharing for an AnalyticDB for PostgreSQL instance in Serverless mode.
        ## Limits
        You can call this operation up to 1,000 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: SetDataShareInstanceRequest
        @return: SetDataShareInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_data_share_instance_with_options_async(request, runtime)

    def switch_dbinstance_net_type_with_options(
        self,
        request: gpdb_20160503_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceNetType',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SwitchDBInstanceNetTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_net_type_with_options_async(
        self,
        request: gpdb_20160503_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchDBInstanceNetType',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SwitchDBInstanceNetTypeResponse(),
            await self.call_api_async(params, req, runtime)
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
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: gpdb_20160503_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.TagResourcesResponse:
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
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def unload_sample_data_with_options(
        self,
        request: gpdb_20160503_models.UnloadSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UnloadSampleDataResponse:
        """
        You can call this operation to release a sample dataset from an AnalyticDB for PostgreSQL instance. You must have already loaded the sample dataset.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnloadSampleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnloadSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnloadSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UnloadSampleDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def unload_sample_data_with_options_async(
        self,
        request: gpdb_20160503_models.UnloadSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UnloadSampleDataResponse:
        """
        You can call this operation to release a sample dataset from an AnalyticDB for PostgreSQL instance. You must have already loaded the sample dataset.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnloadSampleDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnloadSampleDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnloadSampleData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UnloadSampleDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unload_sample_data(
        self,
        request: gpdb_20160503_models.UnloadSampleDataRequest,
    ) -> gpdb_20160503_models.UnloadSampleDataResponse:
        """
        You can call this operation to release a sample dataset from an AnalyticDB for PostgreSQL instance. You must have already loaded the sample dataset.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnloadSampleDataRequest
        @return: UnloadSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unload_sample_data_with_options(request, runtime)

    async def unload_sample_data_async(
        self,
        request: gpdb_20160503_models.UnloadSampleDataRequest,
    ) -> gpdb_20160503_models.UnloadSampleDataResponse:
        """
        You can call this operation to release a sample dataset from an AnalyticDB for PostgreSQL instance. You must have already loaded the sample dataset.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnloadSampleDataRequest
        @return: UnloadSampleDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unload_sample_data_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: gpdb_20160503_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UntagResourcesResponse:
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
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: gpdb_20160503_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UntagResourcesResponse:
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
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_collection_data_metadata_with_options(
        self,
        tmp_req: gpdb_20160503_models.UpdateCollectionDataMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpdateCollectionDataMetadataResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpdateCollectionDataMetadataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not UtilClient.is_unset(tmp_req.metadata):
            request.metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.metadata_shrink):
            query['Metadata'] = request.metadata_shrink
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCollectionDataMetadata',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpdateCollectionDataMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_collection_data_metadata_with_options_async(
        self,
        tmp_req: gpdb_20160503_models.UpdateCollectionDataMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpdateCollectionDataMetadataResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpdateCollectionDataMetadataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        if not UtilClient.is_unset(tmp_req.metadata):
            request.metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metadata, 'Metadata', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.metadata_shrink):
            query['Metadata'] = request.metadata_shrink
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCollectionDataMetadata',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpdateCollectionDataMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_collection_data_metadata(
        self,
        request: gpdb_20160503_models.UpdateCollectionDataMetadataRequest,
    ) -> gpdb_20160503_models.UpdateCollectionDataMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_collection_data_metadata_with_options(request, runtime)

    async def update_collection_data_metadata_async(
        self,
        request: gpdb_20160503_models.UpdateCollectionDataMetadataRequest,
    ) -> gpdb_20160503_models.UpdateCollectionDataMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_collection_data_metadata_with_options_async(request, runtime)

    def update_dbinstance_plan_with_options(
        self,
        request: gpdb_20160503_models.UpdateDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpdateDBInstancePlanResponse:
        """
        You can call this operation to modify a plan for an AnalyticDB for PostgreSQL instance in Serverless mode. For example, you can modify a plan for periodically pausing and resuming an instance or scaling an instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateDBInstancePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpdateDBInstancePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dbinstance_plan_with_options_async(
        self,
        request: gpdb_20160503_models.UpdateDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpdateDBInstancePlanResponse:
        """
        You can call this operation to modify a plan for an AnalyticDB for PostgreSQL instance in Serverless mode. For example, you can modify a plan for periodically pausing and resuming an instance or scaling an instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateDBInstancePlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDBInstancePlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.plan_config):
            query['PlanConfig'] = request.plan_config
        if not UtilClient.is_unset(request.plan_desc):
            query['PlanDesc'] = request.plan_desc
        if not UtilClient.is_unset(request.plan_end_date):
            query['PlanEndDate'] = request.plan_end_date
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_name):
            query['PlanName'] = request.plan_name
        if not UtilClient.is_unset(request.plan_start_date):
            query['PlanStartDate'] = request.plan_start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDBInstancePlan',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpdateDBInstancePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dbinstance_plan(
        self,
        request: gpdb_20160503_models.UpdateDBInstancePlanRequest,
    ) -> gpdb_20160503_models.UpdateDBInstancePlanResponse:
        """
        You can call this operation to modify a plan for an AnalyticDB for PostgreSQL instance in Serverless mode. For example, you can modify a plan for periodically pausing and resuming an instance or scaling an instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateDBInstancePlanRequest
        @return: UpdateDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_plan_with_options(request, runtime)

    async def update_dbinstance_plan_async(
        self,
        request: gpdb_20160503_models.UpdateDBInstancePlanRequest,
    ) -> gpdb_20160503_models.UpdateDBInstancePlanResponse:
        """
        You can call this operation to modify a plan for an AnalyticDB for PostgreSQL instance in Serverless mode. For example, you can modify a plan for periodically pausing and resuming an instance or scaling an instance.
        ## Limits
        You can call this operation up to 1,000 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateDBInstancePlanRequest
        @return: UpdateDBInstancePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dbinstance_plan_with_options_async(request, runtime)

    def upgrade_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        """
        This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: UpgradeDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        """
        This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: UpgradeDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_group_count):
            query['DBInstanceGroupCount'] = request.dbinstance_group_count
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.master_node_num):
            query['MasterNodeNum'] = request.master_node_num
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.seg_disk_performance_level):
            query['SegDiskPerformanceLevel'] = request.seg_disk_performance_level
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstance',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        """
        This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: UpgradeDBInstanceRequest
        @return: UpgradeDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_with_options(request, runtime)

    async def upgrade_dbinstance_async(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        """
        This operation is not available for instances in reserved storage mode.
        Before you call this operation, make sure that you are familiar with the billing of AnalyticDB for PostgreSQL. For more information, see [Billing methods](~~35406~~) and [AnalyticDB for PostgreSQL pricing](https://www.alibabacloud.com/zh/product/hybriddb-postgresql/pricing).
        
        @param request: UpgradeDBInstanceRequest
        @return: UpgradeDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_with_options_async(request, runtime)

    def upgrade_dbversion_with_options(
        self,
        request: gpdb_20160503_models.UpgradeDBVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBVersion',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbversion_with_options_async(
        self,
        request: gpdb_20160503_models.UpgradeDBVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.major_version):
            query['MajorVersion'] = request.major_version
        if not UtilClient.is_unset(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBVersion',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBVersionResponse(),
            await self.call_api_async(params, req, runtime)
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

    def upsert_chunks_with_options(
        self,
        tmp_req: gpdb_20160503_models.UpsertChunksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpsertChunksResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpsertChunksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.text_chunks):
            request.text_chunks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_chunks, 'TextChunks', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.text_chunks_shrink):
            body['TextChunks'] = request.text_chunks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertChunks',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpsertChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_chunks_with_options_async(
        self,
        tmp_req: gpdb_20160503_models.UpsertChunksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpsertChunksResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpsertChunksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.text_chunks):
            request.text_chunks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_chunks, 'TextChunks', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.text_chunks_shrink):
            body['TextChunks'] = request.text_chunks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertChunks',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpsertChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_chunks(
        self,
        request: gpdb_20160503_models.UpsertChunksRequest,
    ) -> gpdb_20160503_models.UpsertChunksResponse:
        runtime = util_models.RuntimeOptions()
        return self.upsert_chunks_with_options(request, runtime)

    async def upsert_chunks_async(
        self,
        request: gpdb_20160503_models.UpsertChunksRequest,
    ) -> gpdb_20160503_models.UpsertChunksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upsert_chunks_with_options_async(request, runtime)

    def upsert_collection_data_with_options(
        self,
        tmp_req: gpdb_20160503_models.UpsertCollectionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpsertCollectionDataResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpsertCollectionDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rows):
            request.rows_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rows, 'Rows', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.rows_shrink):
            body['Rows'] = request.rows_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpsertCollectionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_collection_data_with_options_async(
        self,
        tmp_req: gpdb_20160503_models.UpsertCollectionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpsertCollectionDataResponse:
        UtilClient.validate_model(tmp_req)
        request = gpdb_20160503_models.UpsertCollectionDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rows):
            request.rows_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rows, 'Rows', 'json')
        query = {}
        if not UtilClient.is_unset(request.collection):
            query['Collection'] = request.collection
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_password):
            query['NamespacePassword'] = request.namespace_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.rows_shrink):
            body['Rows'] = request.rows_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertCollectionData',
            version='2016-05-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpsertCollectionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_collection_data(
        self,
        request: gpdb_20160503_models.UpsertCollectionDataRequest,
    ) -> gpdb_20160503_models.UpsertCollectionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.upsert_collection_data_with_options(request, runtime)

    async def upsert_collection_data_async(
        self,
        request: gpdb_20160503_models.UpsertCollectionDataRequest,
    ) -> gpdb_20160503_models.UpsertCollectionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upsert_collection_data_with_options_async(request, runtime)
