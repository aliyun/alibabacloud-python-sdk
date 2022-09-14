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

    def add_bu_dbinstance_relation_with_options(
        self,
        request: gpdb_20160503_models.AddBuDBInstanceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AddBuDBInstanceRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_unit):
            query['BusinessUnit'] = request.business_unit
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBuDBInstanceRelation',
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
            gpdb_20160503_models.AddBuDBInstanceRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_bu_dbinstance_relation_with_options_async(
        self,
        request: gpdb_20160503_models.AddBuDBInstanceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AddBuDBInstanceRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_unit):
            query['BusinessUnit'] = request.business_unit
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBuDBInstanceRelation',
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
            gpdb_20160503_models.AddBuDBInstanceRelationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
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
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
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
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
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
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
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
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_dbinstance_plan_with_options(
        self,
        request: gpdb_20160503_models.CreateDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDBInstancePlanResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_plan_with_options(request, runtime)

    async def create_dbinstance_plan_async(
        self,
        request: gpdb_20160503_models.CreateDBInstancePlanRequest,
    ) -> gpdb_20160503_models.CreateDBInstancePlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_plan_with_options_async(request, runtime)

    def create_ecsdbinstance_with_options(
        self,
        request: gpdb_20160503_models.CreateECSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateECSDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_category):
            query['DBInstanceCategory'] = request.dbinstance_category
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
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
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
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
            action='CreateECSDBInstance',
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
            gpdb_20160503_models.CreateECSDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ecsdbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.CreateECSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateECSDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_category):
            query['DBInstanceCategory'] = request.dbinstance_category
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not UtilClient.is_unset(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
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
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
        if not UtilClient.is_unset(request.seg_storage_type):
            query['SegStorageType'] = request.seg_storage_type
        if not UtilClient.is_unset(request.src_db_instance_name):
            query['SrcDbInstanceName'] = request.src_db_instance_name
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
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
            action='CreateECSDBInstance',
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
            gpdb_20160503_models.CreateECSDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_sample_data_with_options(
        self,
        request: gpdb_20160503_models.CreateSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateSampleDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_sample_data_with_options(request, runtime)

    async def create_sample_data_async(
        self,
        request: gpdb_20160503_models.CreateSampleDataRequest,
    ) -> gpdb_20160503_models.CreateSampleDataResponse:
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

    def delete_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_dbinstance_plan_with_options(
        self,
        request: gpdb_20160503_models.DeleteDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstancePlanResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_plan_with_options(request, runtime)

    async def delete_dbinstance_plan_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstancePlanRequest,
    ) -> gpdb_20160503_models.DeleteDBInstancePlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_plan_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: gpdb_20160503_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
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
            gpdb_20160503_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
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
            gpdb_20160503_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_accounts_with_options(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_dbcluster_node_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterNodeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_node_with_options(request, runtime)

    async def describe_dbcluster_node_async(
        self,
        request: gpdb_20160503_models.DescribeDBClusterNodeRequest,
    ) -> gpdb_20160503_models.DescribeDBClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_node_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_data_bloat_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataBloatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataBloatResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_bloat_with_options(request, runtime)

    async def describe_dbinstance_data_bloat_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataBloatRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataBloatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_data_bloat_with_options_async(request, runtime)

    def describe_dbinstance_data_skew_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataSkewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataSkewResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_skew_with_options(request, runtime)

    async def describe_dbinstance_data_skew_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDataSkewRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDataSkewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_data_skew_with_options_async(request, runtime)

    def describe_dbinstance_diagnosis_summary_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_diagnosis_summary_with_options(request, runtime)

    async def describe_dbinstance_diagnosis_summary_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceDiagnosisSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_diagnosis_summary_with_options_async(request, runtime)

    def describe_dbinstance_error_log_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceErrorLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceErrorLogResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_error_log_with_options(request, runtime)

    async def describe_dbinstance_error_log_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceErrorLogRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceErrorLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_error_log_with_options_async(request, runtime)

    def describe_dbinstance_iparray_list_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    async def describe_dbinstance_iparray_list_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_iparray_list_with_options_async(request, runtime)

    def describe_dbinstance_index_usage_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIndexUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_index_usage_with_options(request, runtime)

    async def describe_dbinstance_index_usage_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIndexUsageRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIndexUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_index_usage_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
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

    def describe_dbinstance_on_ecsattribute_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceOnECSAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse:
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
            action='DescribeDBInstanceOnECSAttribute',
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
            gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_on_ecsattribute_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceOnECSAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse:
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
            action='DescribeDBInstanceOnECSAttribute',
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
            gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_plans_with_options(request, runtime)

    async def describe_dbinstance_plans_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePlansRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancePlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_plans_with_options_async(request, runtime)

    def describe_dbinstance_sqlpatterns_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDBInstanceSQLPatterns',
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
            gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_sqlpatterns_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeDBInstanceSQLPatterns',
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
            gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_dbinstances_with_options(
        self,
        tmp_req: gpdb_20160503_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_data_backups_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_data_backups_with_options(request, runtime)

    async def describe_data_backups_async(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_backups_with_options_async(request, runtime)

    def describe_data_share_instances_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataShareInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataShareInstancesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_data_share_instances_with_options(request, runtime)

    async def describe_data_share_instances_async(
        self,
        request: gpdb_20160503_models.DescribeDataShareInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDataShareInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_share_instances_with_options_async(request, runtime)

    def describe_data_share_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataSharePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataSharePerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_data_share_performance_with_options(request, runtime)

    async def describe_data_share_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDataSharePerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDataSharePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_share_performance_with_options_async(request, runtime)

    def describe_diagnosis_dimensions_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisDimensionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    async def describe_diagnosis_dimensions_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisDimensionsRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisDimensionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_dimensions_with_options_async(request, runtime)

    def describe_diagnosis_monitor_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_monitor_performance_with_options(request, runtime)

    async def describe_diagnosis_monitor_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisMonitorPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_monitor_performance_with_options_async(request, runtime)

    def describe_diagnosis_records_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisRecordsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    async def describe_diagnosis_records_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisRecordsRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_records_with_options_async(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    async def describe_diagnosis_sqlinfo_async(
        self,
        request: gpdb_20160503_models.DescribeDiagnosisSQLInfoRequest,
    ) -> gpdb_20160503_models.DescribeDiagnosisSQLInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_sqlinfo_with_options_async(request, runtime)

    def describe_download_records_with_options(
        self,
        request: gpdb_20160503_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDownloadRecordsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    async def describe_download_records_async(
        self,
        request: gpdb_20160503_models.DescribeDownloadRecordsRequest,
    ) -> gpdb_20160503_models.DescribeDownloadRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_records_with_options_async(request, runtime)

    def describe_health_status_with_options(
        self,
        request: gpdb_20160503_models.DescribeHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeHealthStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    async def describe_health_status_async(
        self,
        request: gpdb_20160503_models.DescribeHealthStatusRequest,
    ) -> gpdb_20160503_models.DescribeHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_status_with_options_async(request, runtime)

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

    def describe_parameters_with_options(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_rds_vswitchs_with_options(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vswitchs_with_options(request, runtime)

    async def describe_rds_vswitchs_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vswitchs_with_options_async(request, runtime)

    def describe_rds_vpcs_with_options(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpcs_with_options(request, runtime)

    async def describe_rds_vpcs_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vpcs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsage',
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
            gpdb_20160503_models.DescribeResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_usage_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsage',
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
            gpdb_20160503_models.DescribeResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_sqlcollector_policy_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorPolicy',
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
            gpdb_20160503_models.DescribeSQLCollectorPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlcollector_policy_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLCollectorPolicy',
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
            gpdb_20160503_models.DescribeSQLCollectorPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogByQueryId',
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
            gpdb_20160503_models.DescribeSQLLogByQueryIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_by_query_id_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogByQueryIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogByQueryIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogByQueryId',
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
            gpdb_20160503_models.DescribeSQLLogByQueryIdResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogFiles',
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
            gpdb_20160503_models.DescribeSQLLogFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_files_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogFiles',
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
            gpdb_20160503_models.DescribeSQLLogFilesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogRecords',
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
            gpdb_20160503_models.DescribeSQLLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllog_records_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.form):
            query['Form'] = request.form
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogRecords',
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
            gpdb_20160503_models.DescribeSQLLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        if not UtilClient.is_unset(request.slice_id):
            query['SliceId'] = request.slice_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogsOnSlice',
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
            gpdb_20160503_models.DescribeSQLLogsOnSliceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqllogs_on_slice_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsOnSliceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsOnSliceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.execute_state):
            query['ExecuteState'] = request.execute_state
        if not UtilClient.is_unset(request.max_execute_cost):
            query['MaxExecuteCost'] = request.max_execute_cost
        if not UtilClient.is_unset(request.min_execute_cost):
            query['MinExecuteCost'] = request.min_execute_cost
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        if not UtilClient.is_unset(request.slice_id):
            query['SliceId'] = request.slice_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLLogsOnSlice',
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
            gpdb_20160503_models.DescribeSQLLogsOnSliceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_sample_data_with_options(
        self,
        request: gpdb_20160503_models.DescribeSampleDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSampleDataResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_sample_data_with_options(request, runtime)

    async def describe_sample_data_async(
        self,
        request: gpdb_20160503_models.DescribeSampleDataRequest,
    ) -> gpdb_20160503_models.DescribeSampleDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sample_data_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: gpdb_20160503_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            query['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
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
            gpdb_20160503_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqlid):
            query['SQLId'] = request.sqlid
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
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
            gpdb_20160503_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeSlowSQLLogs',
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
            gpdb_20160503_models.DescribeSlowSQLLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_sqllogs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSlowSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSlowSQLLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='DescribeSlowSQLLogs',
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
            gpdb_20160503_models.DescribeSlowSQLLogsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.cpu_cores):
            query['CpuCores'] = request.cpu_cores
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.total_node_num):
            query['TotalNodeNum'] = request.total_node_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpecification',
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
            gpdb_20160503_models.DescribeSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_specification_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSpecificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_cores):
            query['CpuCores'] = request.cpu_cores
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.total_node_num):
            query['TotalNodeNum'] = request.total_node_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSpecification',
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
            gpdb_20160503_models.DescribeSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
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

    def download_diagnosis_records_with_options(
        self,
        request: gpdb_20160503_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DownloadDiagnosisRecordsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    async def download_diagnosis_records_async(
        self,
        request: gpdb_20160503_models.DownloadDiagnosisRecordsRequest,
    ) -> gpdb_20160503_models.DownloadDiagnosisRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_diagnosis_records_with_options_async(request, runtime)

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

    def modify_dbinstance_connection_mode_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionMode',
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
            gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_mode_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_mode):
            query['ConnectionMode'] = request.connection_mode
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionMode',
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
            gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
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
            gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_network_type):
            query['InstanceNetworkType'] = request.instance_network_type
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceNetworkType',
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
            gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_dbinstance_resource_group_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_resource_group_with_options(request, runtime)

    async def modify_dbinstance_resource_group_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceResourceGroupRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceResourceGroupResponse:
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

    def modify_parameters_with_options(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_iparray_attribute):
            query['DBInstanceIPArrayAttribute'] = request.dbinstance_iparray_attribute
        if not UtilClient.is_unset(request.dbinstance_iparray_name):
            query['DBInstanceIPArrayName'] = request.dbinstance_iparray_name
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def pause_instance_with_options(
        self,
        request: gpdb_20160503_models.PauseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.PauseInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.pause_instance_with_options(request, runtime)

    async def pause_instance_async(
        self,
        request: gpdb_20160503_models.PauseInstanceRequest,
    ) -> gpdb_20160503_models.PauseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pause_instance_with_options_async(request, runtime)

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

    def restart_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def resume_instance_with_options(
        self,
        request: gpdb_20160503_models.ResumeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResumeInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    async def resume_instance_async(
        self,
        request: gpdb_20160503_models.ResumeInstanceRequest,
    ) -> gpdb_20160503_models.ResumeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_instance_with_options_async(request, runtime)

    def set_dbinstance_plan_status_with_options(
        self,
        request: gpdb_20160503_models.SetDBInstancePlanStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SetDBInstancePlanStatusResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_dbinstance_plan_status_with_options(request, runtime)

    async def set_dbinstance_plan_status_async(
        self,
        request: gpdb_20160503_models.SetDBInstancePlanStatusRequest,
    ) -> gpdb_20160503_models.SetDBInstancePlanStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dbinstance_plan_status_with_options_async(request, runtime)

    def set_data_share_instance_with_options(
        self,
        tmp_req: gpdb_20160503_models.SetDataShareInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SetDataShareInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.set_data_share_instance_with_options(request, runtime)

    async def set_data_share_instance_async(
        self,
        request: gpdb_20160503_models.SetDataShareInstanceRequest,
    ) -> gpdb_20160503_models.SetDataShareInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.unload_sample_data_with_options(request, runtime)

    async def unload_sample_data_async(
        self,
        request: gpdb_20160503_models.UnloadSampleDataRequest,
    ) -> gpdb_20160503_models.UnloadSampleDataResponse:
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

    def update_dbinstance_plan_with_options(
        self,
        request: gpdb_20160503_models.UpdateDBInstancePlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpdateDBInstancePlanResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_plan_with_options(request, runtime)

    async def update_dbinstance_plan_async(
        self,
        request: gpdb_20160503_models.UpdateDBInstancePlanRequest,
    ) -> gpdb_20160503_models.UpdateDBInstancePlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dbinstance_plan_with_options_async(request, runtime)

    def upgrade_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
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
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
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
        if not UtilClient.is_unset(request.seg_node_num):
            query['SegNodeNum'] = request.seg_node_num
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
