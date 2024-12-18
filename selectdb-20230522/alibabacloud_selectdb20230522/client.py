# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_selectdb20230522 import models as selectdb_20230522_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('selectdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: selectdb_20230522_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for SelectDB instance.
        
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: selectdb_20230522_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for SelectDB instance.
        
        @param request: AllocateInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateInstancePublicConnection',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: selectdb_20230522_models.AllocateInstancePublicConnectionRequest,
    ) -> selectdb_20230522_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for SelectDB instance.
        
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: selectdb_20230522_models.AllocateInstancePublicConnectionRequest,
    ) -> selectdb_20230522_models.AllocateInstancePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for an ApsaraDB for SelectDB instance.
        
        @param request: AllocateInstancePublicConnectionRequest
        @return: AllocateInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def check_create_dbinstance_with_options(
        self,
        request: selectdb_20230522_models.CheckCreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CheckCreateDBInstanceResponse:
        """
        @summary SelectDB实例创建前检查
        
        @param request: CheckCreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CheckCreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_create_dbinstance_with_options_async(
        self,
        request: selectdb_20230522_models.CheckCreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CheckCreateDBInstanceResponse:
        """
        @summary SelectDB实例创建前检查
        
        @param request: CheckCreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCreateDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CheckCreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_create_dbinstance(
        self,
        request: selectdb_20230522_models.CheckCreateDBInstanceRequest,
    ) -> selectdb_20230522_models.CheckCreateDBInstanceResponse:
        """
        @summary SelectDB实例创建前检查
        
        @param request: CheckCreateDBInstanceRequest
        @return: CheckCreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_create_dbinstance_with_options(request, runtime)

    async def check_create_dbinstance_async(
        self,
        request: selectdb_20230522_models.CheckCreateDBInstanceRequest,
    ) -> selectdb_20230522_models.CheckCreateDBInstanceResponse:
        """
        @summary SelectDB实例创建前检查
        
        @param request: CheckCreateDBInstanceRequest
        @return: CheckCreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_create_dbinstance_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: selectdb_20230522_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CheckServiceLinkedRoleResponse:
        """
        @summary 检查服务关联角色
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: selectdb_20230522_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CheckServiceLinkedRoleResponse:
        """
        @summary 检查服务关联角色
        
        @param request: CheckServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceLinkedRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: selectdb_20230522_models.CheckServiceLinkedRoleRequest,
    ) -> selectdb_20230522_models.CheckServiceLinkedRoleResponse:
        """
        @summary 检查服务关联角色
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: selectdb_20230522_models.CheckServiceLinkedRoleRequest,
    ) -> selectdb_20230522_models.CheckServiceLinkedRoleResponse:
        """
        @summary 检查服务关联角色
        
        @param request: CheckServiceLinkedRoleRequest
        @return: CheckServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: selectdb_20230522_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateDBClusterResponse:
        """
        @summary Creates a cluster in an ApsaraDB for SelectDB instance.
        
        @description > : For an instance that uses the pay-as-you-go billing method, you can create only pay-as-you-go clusters. For an instance that uses the subscription billing method, you can create pay-as-you-go or subscription clusters.
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: selectdb_20230522_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateDBClusterResponse:
        """
        @summary Creates a cluster in an ApsaraDB for SelectDB instance.
        
        @description > : For an instance that uses the pay-as-you-go billing method, you can create only pay-as-you-go clusters. For an instance that uses the subscription billing method, you can create pay-as-you-go or subscription clusters.
        
        @param request: CreateDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster(
        self,
        request: selectdb_20230522_models.CreateDBClusterRequest,
    ) -> selectdb_20230522_models.CreateDBClusterResponse:
        """
        @summary Creates a cluster in an ApsaraDB for SelectDB instance.
        
        @description > : For an instance that uses the pay-as-you-go billing method, you can create only pay-as-you-go clusters. For an instance that uses the subscription billing method, you can create pay-as-you-go or subscription clusters.
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: selectdb_20230522_models.CreateDBClusterRequest,
    ) -> selectdb_20230522_models.CreateDBClusterResponse:
        """
        @summary Creates a cluster in an ApsaraDB for SelectDB instance.
        
        @description > : For an instance that uses the pay-as-you-go billing method, you can create only pay-as-you-go clusters. For an instance that uses the subscription billing method, you can create pay-as-you-go or subscription clusters.
        
        @param request: CreateDBClusterRequest
        @return: CreateDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        tmp_req: selectdb_20230522_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建SelectDB实例
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = selectdb_20230522_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        tmp_req: selectdb_20230522_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建SelectDB实例
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = selectdb_20230522_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: selectdb_20230522_models.CreateDBInstanceRequest,
    ) -> selectdb_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建SelectDB实例
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: selectdb_20230522_models.CreateDBInstanceRequest,
    ) -> selectdb_20230522_models.CreateDBInstanceResponse:
        """
        @summary 创建SelectDB实例
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_elastic_rule_with_options(
        self,
        request: selectdb_20230522_models.CreateElasticRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateElasticRuleResponse:
        """
        @summary 创建分时弹性规则
        
        @param request: CreateElasticRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not UtilClient.is_unset(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticRule',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateElasticRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_rule_with_options_async(
        self,
        request: selectdb_20230522_models.CreateElasticRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateElasticRuleResponse:
        """
        @summary 创建分时弹性规则
        
        @param request: CreateElasticRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not UtilClient.is_unset(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateElasticRule',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateElasticRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_rule(
        self,
        request: selectdb_20230522_models.CreateElasticRuleRequest,
    ) -> selectdb_20230522_models.CreateElasticRuleResponse:
        """
        @summary 创建分时弹性规则
        
        @param request: CreateElasticRuleRequest
        @return: CreateElasticRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_elastic_rule_with_options(request, runtime)

    async def create_elastic_rule_async(
        self,
        request: selectdb_20230522_models.CreateElasticRuleRequest,
    ) -> selectdb_20230522_models.CreateElasticRuleResponse:
        """
        @summary 创建分时弹性规则
        
        @param request: CreateElasticRuleRequest
        @return: CreateElasticRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_elastic_rule_with_options_async(request, runtime)

    def create_service_linked_role_for_select_dbwith_options(
        self,
        request: selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBResponse:
        """
        @summary Creates a service-linked role for ApsaraDB for SelectDB.
        
        @param request: CreateServiceLinkedRoleForSelectDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleForSelectDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRoleForSelectDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_for_select_dbwith_options_async(
        self,
        request: selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBResponse:
        """
        @summary Creates a service-linked role for ApsaraDB for SelectDB.
        
        @param request: CreateServiceLinkedRoleForSelectDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceLinkedRoleForSelectDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRoleForSelectDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role_for_select_db(
        self,
        request: selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBRequest,
    ) -> selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBResponse:
        """
        @summary Creates a service-linked role for ApsaraDB for SelectDB.
        
        @param request: CreateServiceLinkedRoleForSelectDBRequest
        @return: CreateServiceLinkedRoleForSelectDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_for_select_dbwith_options(request, runtime)

    async def create_service_linked_role_for_select_db_async(
        self,
        request: selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBRequest,
    ) -> selectdb_20230522_models.CreateServiceLinkedRoleForSelectDBResponse:
        """
        @summary Creates a service-linked role for ApsaraDB for SelectDB.
        
        @param request: CreateServiceLinkedRoleForSelectDBRequest
        @return: CreateServiceLinkedRoleForSelectDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_for_select_dbwith_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: selectdb_20230522_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DeleteDBClusterResponse:
        """
        @summary 释放实例下集群
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: selectdb_20230522_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DeleteDBClusterResponse:
        """
        @summary 释放实例下集群
        
        @param request: DeleteDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: selectdb_20230522_models.DeleteDBClusterRequest,
    ) -> selectdb_20230522_models.DeleteDBClusterResponse:
        """
        @summary 释放实例下集群
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: selectdb_20230522_models.DeleteDBClusterRequest,
    ) -> selectdb_20230522_models.DeleteDBClusterResponse:
        """
        @summary 释放实例下集群
        
        @param request: DeleteDBClusterRequest
        @return: DeleteDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: selectdb_20230522_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 删除DB实例
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: selectdb_20230522_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 删除DB实例
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: selectdb_20230522_models.DeleteDBInstanceRequest,
    ) -> selectdb_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 删除DB实例
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: selectdb_20230522_models.DeleteDBInstanceRequest,
    ) -> selectdb_20230522_models.DeleteDBInstanceResponse:
        """
        @summary 删除DB实例
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_elastic_rule_with_options(
        self,
        request: selectdb_20230522_models.DeleteElasticRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DeleteElasticRuleResponse:
        """
        @summary 删除分时弹性规则
        
        @param request: DeleteElasticRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteElasticRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticRule',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DeleteElasticRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_rule_with_options_async(
        self,
        request: selectdb_20230522_models.DeleteElasticRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DeleteElasticRuleResponse:
        """
        @summary 删除分时弹性规则
        
        @param request: DeleteElasticRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteElasticRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteElasticRule',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DeleteElasticRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_rule(
        self,
        request: selectdb_20230522_models.DeleteElasticRuleRequest,
    ) -> selectdb_20230522_models.DeleteElasticRuleResponse:
        """
        @summary 删除分时弹性规则
        
        @param request: DeleteElasticRuleRequest
        @return: DeleteElasticRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_elastic_rule_with_options(request, runtime)

    async def delete_elastic_rule_async(
        self,
        request: selectdb_20230522_models.DeleteElasticRuleRequest,
    ) -> selectdb_20230522_models.DeleteElasticRuleResponse:
        """
        @summary 删除分时弹性规则
        
        @param request: DeleteElasticRuleRequest
        @return: DeleteElasticRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_elastic_rule_with_options_async(request, runtime)

    def describe_all_dbinstance_class_with_options(
        self,
        request: selectdb_20230522_models.DescribeAllDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeAllDBInstanceClassResponse:
        """
        @summary Queries the information about all instance specifications.
        
        @param request: DescribeAllDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDBInstanceClass',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeAllDBInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_dbinstance_class_with_options_async(
        self,
        request: selectdb_20230522_models.DescribeAllDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeAllDBInstanceClassResponse:
        """
        @summary Queries the information about all instance specifications.
        
        @param request: DescribeAllDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAllDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAllDBInstanceClass',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeAllDBInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_dbinstance_class(
        self,
        request: selectdb_20230522_models.DescribeAllDBInstanceClassRequest,
    ) -> selectdb_20230522_models.DescribeAllDBInstanceClassResponse:
        """
        @summary Queries the information about all instance specifications.
        
        @param request: DescribeAllDBInstanceClassRequest
        @return: DescribeAllDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_all_dbinstance_class_with_options(request, runtime)

    async def describe_all_dbinstance_class_async(
        self,
        request: selectdb_20230522_models.DescribeAllDBInstanceClassRequest,
    ) -> selectdb_20230522_models.DescribeAllDBInstanceClassResponse:
        """
        @summary Queries the information about all instance specifications.
        
        @param request: DescribeAllDBInstanceClassRequest
        @return: DescribeAllDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_dbinstance_class_with_options_async(request, runtime)

    def describe_dbcluster_config_with_options(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries the configuration information about a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_with_options_async(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries the configuration information about a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigRequest,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries the configuration information about a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigRequest
        @return: DescribeDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_with_options(request, runtime)

    async def describe_dbcluster_config_async(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigRequest,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigResponse:
        """
        @summary Queries the configuration information about a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigRequest
        @return: DescribeDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_config_with_options_async(request, runtime)

    def describe_dbcluster_config_change_logs_with_options(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigChangeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigChangeLogsResponse:
        """
        @summary Queries the configuration change logs of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigChangeLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigChangeLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfigChangeLogs',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBClusterConfigChangeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_change_logs_with_options_async(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigChangeLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigChangeLogsResponse:
        """
        @summary Queries the configuration change logs of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigChangeLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBClusterConfigChangeLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfigChangeLogs',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBClusterConfigChangeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config_change_logs(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigChangeLogsRequest,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigChangeLogsResponse:
        """
        @summary Queries the configuration change logs of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigChangeLogsRequest
        @return: DescribeDBClusterConfigChangeLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_change_logs_with_options(request, runtime)

    async def describe_dbcluster_config_change_logs_async(
        self,
        request: selectdb_20230522_models.DescribeDBClusterConfigChangeLogsRequest,
    ) -> selectdb_20230522_models.DescribeDBClusterConfigChangeLogsResponse:
        """
        @summary Queries the configuration change logs of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBClusterConfigChangeLogsRequest
        @return: DescribeDBClusterConfigChangeLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_config_change_logs_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceAttributeRequest,
    ) -> selectdb_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceAttributeRequest,
    ) -> selectdb_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceNetInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceNetInfo',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBInstanceNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceNetInfoRequest,
    ) -> selectdb_20230522_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @return: DescribeDBInstanceNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: selectdb_20230522_models.DescribeDBInstanceNetInfoRequest,
    ) -> selectdb_20230522_models.DescribeDBInstanceNetInfoResponse:
        """
        @summary Queries the network information about an ApsaraDB for SelectDB instance.
        
        @param request: DescribeDBInstanceNetInfoRequest
        @return: DescribeDBInstanceNetInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        tmp_req: selectdb_20230522_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries the information about ApsaraDB for SelectDB instances.
        
        @param tmp_req: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = selectdb_20230522_models.DescribeDBInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        tmp_req: selectdb_20230522_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries the information about ApsaraDB for SelectDB instances.
        
        @param tmp_req: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = selectdb_20230522_models.DescribeDBInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: selectdb_20230522_models.DescribeDBInstancesRequest,
    ) -> selectdb_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries the information about ApsaraDB for SelectDB instances.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: selectdb_20230522_models.DescribeDBInstancesRequest,
    ) -> selectdb_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries the information about ApsaraDB for SelectDB instances.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_elastic_rules_with_options(
        self,
        request: selectdb_20230522_models.DescribeElasticRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeElasticRulesResponse:
        """
        @summary 查询分时弹性规则
        
        @param request: DescribeElasticRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticRules',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeElasticRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_rules_with_options_async(
        self,
        request: selectdb_20230522_models.DescribeElasticRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeElasticRulesResponse:
        """
        @summary 查询分时弹性规则
        
        @param request: DescribeElasticRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeElasticRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeElasticRules',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeElasticRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_rules(
        self,
        request: selectdb_20230522_models.DescribeElasticRulesRequest,
    ) -> selectdb_20230522_models.DescribeElasticRulesResponse:
        """
        @summary 查询分时弹性规则
        
        @param request: DescribeElasticRulesRequest
        @return: DescribeElasticRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_rules_with_options(request, runtime)

    async def describe_elastic_rules_async(
        self,
        request: selectdb_20230522_models.DescribeElasticRulesRequest,
    ) -> selectdb_20230522_models.DescribeElasticRulesResponse:
        """
        @summary 查询分时弹性规则
        
        @param request: DescribeElasticRulesRequest
        @return: DescribeElasticRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_rules_with_options_async(request, runtime)

    def describe_security_iplist_with_options(
        self,
        request: selectdb_20230522_models.DescribeSecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the IP addresses in the whitelists of an ApsaraDB for SelectDB instance.
        
        @param request: DescribeSecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeSecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_iplist_with_options_async(
        self,
        request: selectdb_20230522_models.DescribeSecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the IP addresses in the whitelists of an ApsaraDB for SelectDB instance.
        
        @param request: DescribeSecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.DescribeSecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_iplist(
        self,
        request: selectdb_20230522_models.DescribeSecurityIPListRequest,
    ) -> selectdb_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the IP addresses in the whitelists of an ApsaraDB for SelectDB instance.
        
        @param request: DescribeSecurityIPListRequest
        @return: DescribeSecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_iplist_with_options(request, runtime)

    async def describe_security_iplist_async(
        self,
        request: selectdb_20230522_models.DescribeSecurityIPListRequest,
    ) -> selectdb_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the IP addresses in the whitelists of an ApsaraDB for SelectDB instance.
        
        @param request: DescribeSecurityIPListRequest
        @return: DescribeSecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_iplist_with_options_async(request, runtime)

    def en_disable_scaling_rules_with_options(
        self,
        request: selectdb_20230522_models.EnDisableScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.EnDisableScalingRulesResponse:
        """
        @summary 开关分时弹性策略
        
        @param request: EnDisableScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnDisableScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rules_enable):
            query['ScalingRulesEnable'] = request.scaling_rules_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnDisableScalingRules',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.EnDisableScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def en_disable_scaling_rules_with_options_async(
        self,
        request: selectdb_20230522_models.EnDisableScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.EnDisableScalingRulesResponse:
        """
        @summary 开关分时弹性策略
        
        @param request: EnDisableScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnDisableScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rules_enable):
            query['ScalingRulesEnable'] = request.scaling_rules_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnDisableScalingRules',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.EnDisableScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def en_disable_scaling_rules(
        self,
        request: selectdb_20230522_models.EnDisableScalingRulesRequest,
    ) -> selectdb_20230522_models.EnDisableScalingRulesResponse:
        """
        @summary 开关分时弹性策略
        
        @param request: EnDisableScalingRulesRequest
        @return: EnDisableScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.en_disable_scaling_rules_with_options(request, runtime)

    async def en_disable_scaling_rules_async(
        self,
        request: selectdb_20230522_models.EnDisableScalingRulesRequest,
    ) -> selectdb_20230522_models.EnDisableScalingRulesResponse:
        """
        @summary 开关分时弹性策略
        
        @param request: EnDisableScalingRulesRequest
        @return: EnDisableScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.en_disable_scaling_rules_with_options_async(request, runtime)

    def get_create_becluster_inquiry_with_options(
        self,
        request: selectdb_20230522_models.GetCreateBEClusterInquiryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.GetCreateBEClusterInquiryResponse:
        """
        @summary Queries the pricing for creating a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetCreateBEClusterInquiryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateBEClusterInquiryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateBEClusterInquiry',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.GetCreateBEClusterInquiryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_becluster_inquiry_with_options_async(
        self,
        request: selectdb_20230522_models.GetCreateBEClusterInquiryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.GetCreateBEClusterInquiryResponse:
        """
        @summary Queries the pricing for creating a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetCreateBEClusterInquiryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateBEClusterInquiryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateBEClusterInquiry',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.GetCreateBEClusterInquiryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_becluster_inquiry(
        self,
        request: selectdb_20230522_models.GetCreateBEClusterInquiryRequest,
    ) -> selectdb_20230522_models.GetCreateBEClusterInquiryResponse:
        """
        @summary Queries the pricing for creating a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetCreateBEClusterInquiryRequest
        @return: GetCreateBEClusterInquiryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_create_becluster_inquiry_with_options(request, runtime)

    async def get_create_becluster_inquiry_async(
        self,
        request: selectdb_20230522_models.GetCreateBEClusterInquiryRequest,
    ) -> selectdb_20230522_models.GetCreateBEClusterInquiryResponse:
        """
        @summary Queries the pricing for creating a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetCreateBEClusterInquiryRequest
        @return: GetCreateBEClusterInquiryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_create_becluster_inquiry_with_options_async(request, runtime)

    def get_modify_becluster_inquiry_with_options(
        self,
        request: selectdb_20230522_models.GetModifyBEClusterInquiryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.GetModifyBEClusterInquiryResponse:
        """
        @summary Queries the pricing for changing the specifications of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetModifyBEClusterInquiryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModifyBEClusterInquiryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModifyBEClusterInquiry',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.GetModifyBEClusterInquiryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_modify_becluster_inquiry_with_options_async(
        self,
        request: selectdb_20230522_models.GetModifyBEClusterInquiryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.GetModifyBEClusterInquiryResponse:
        """
        @summary Queries the pricing for changing the specifications of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetModifyBEClusterInquiryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModifyBEClusterInquiryResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModifyBEClusterInquiry',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.GetModifyBEClusterInquiryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_modify_becluster_inquiry(
        self,
        request: selectdb_20230522_models.GetModifyBEClusterInquiryRequest,
    ) -> selectdb_20230522_models.GetModifyBEClusterInquiryResponse:
        """
        @summary Queries the pricing for changing the specifications of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetModifyBEClusterInquiryRequest
        @return: GetModifyBEClusterInquiryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_modify_becluster_inquiry_with_options(request, runtime)

    async def get_modify_becluster_inquiry_async(
        self,
        request: selectdb_20230522_models.GetModifyBEClusterInquiryRequest,
    ) -> selectdb_20230522_models.GetModifyBEClusterInquiryResponse:
        """
        @summary Queries the pricing for changing the specifications of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: GetModifyBEClusterInquiryRequest
        @return: GetModifyBEClusterInquiryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_modify_becluster_inquiry_with_options_async(request, runtime)

    def modify_becluster_attribute_with_options(
        self,
        request: selectdb_20230522_models.ModifyBEClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyBEClusterAttributeResponse:
        """
        @summary Modifies the name of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyBEClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBEClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBEClusterAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyBEClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_becluster_attribute_with_options_async(
        self,
        request: selectdb_20230522_models.ModifyBEClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyBEClusterAttributeResponse:
        """
        @summary Modifies the name of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyBEClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBEClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBEClusterAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyBEClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_becluster_attribute(
        self,
        request: selectdb_20230522_models.ModifyBEClusterAttributeRequest,
    ) -> selectdb_20230522_models.ModifyBEClusterAttributeResponse:
        """
        @summary Modifies the name of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyBEClusterAttributeRequest
        @return: ModifyBEClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_becluster_attribute_with_options(request, runtime)

    async def modify_becluster_attribute_async(
        self,
        request: selectdb_20230522_models.ModifyBEClusterAttributeRequest,
    ) -> selectdb_20230522_models.ModifyBEClusterAttributeResponse:
        """
        @summary Modifies the name of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyBEClusterAttributeRequest
        @return: ModifyBEClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_becluster_attribute_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: selectdb_20230522_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyDBClusterResponse:
        """
        @summary 集群变配
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: selectdb_20230522_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyDBClusterResponse:
        """
        @summary 集群变配
        
        @param request: ModifyDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not UtilClient.is_unset(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: selectdb_20230522_models.ModifyDBClusterRequest,
    ) -> selectdb_20230522_models.ModifyDBClusterResponse:
        """
        @summary 集群变配
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: selectdb_20230522_models.ModifyDBClusterRequest,
    ) -> selectdb_20230522_models.ModifyDBClusterResponse:
        """
        @summary 集群变配
        
        @param request: ModifyDBClusterRequest
        @return: ModifyDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_config_with_options(
        self,
        request: selectdb_20230522_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_config_with_options_async(
        self,
        request: selectdb_20230522_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBClusterConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_key):
            query['ConfigKey'] = request.config_key
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_config(
        self,
        request: selectdb_20230522_models.ModifyDBClusterConfigRequest,
    ) -> selectdb_20230522_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBClusterConfigRequest
        @return: ModifyDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    async def modify_dbcluster_config_async(
        self,
        request: selectdb_20230522_models.ModifyDBClusterConfigRequest,
    ) -> selectdb_20230522_models.ModifyDBClusterConfigResponse:
        """
        @summary Modifies the configurations of a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBClusterConfigRequest
        @return: ModifyDBClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_config_with_options_async(request, runtime)

    def modify_dbinstance_attribute_with_options(
        self,
        request: selectdb_20230522_models.ModifyDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the maintenance window or description of an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_attribute_with_options_async(
        self,
        request: selectdb_20230522_models.ModifyDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the maintenance window or description of an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_attribute(
        self,
        request: selectdb_20230522_models.ModifyDBInstanceAttributeRequest,
    ) -> selectdb_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the maintenance window or description of an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBInstanceAttributeRequest
        @return: ModifyDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_attribute_with_options(request, runtime)

    async def modify_dbinstance_attribute_async(
        self,
        request: selectdb_20230522_models.ModifyDBInstanceAttributeRequest,
    ) -> selectdb_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the maintenance window or description of an ApsaraDB for SelectDB instance.
        
        @param request: ModifyDBInstanceAttributeRequest
        @return: ModifyDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_attribute_with_options_async(request, runtime)

    def modify_elastic_rule_with_options(
        self,
        request: selectdb_20230522_models.ModifyElasticRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyElasticRuleResponse:
        """
        @summary 修改分时弹性规则
        
        @param request: ModifyElasticRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not UtilClient.is_unset(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticRule',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyElasticRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_rule_with_options_async(
        self,
        request: selectdb_20230522_models.ModifyElasticRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifyElasticRuleResponse:
        """
        @summary 修改分时弹性规则
        
        @param request: ModifyElasticRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not UtilClient.is_unset(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyElasticRule',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifyElasticRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_rule(
        self,
        request: selectdb_20230522_models.ModifyElasticRuleRequest,
    ) -> selectdb_20230522_models.ModifyElasticRuleResponse:
        """
        @summary 修改分时弹性规则
        
        @param request: ModifyElasticRuleRequest
        @return: ModifyElasticRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_rule_with_options(request, runtime)

    async def modify_elastic_rule_async(
        self,
        request: selectdb_20230522_models.ModifyElasticRuleRequest,
    ) -> selectdb_20230522_models.ModifyElasticRuleResponse:
        """
        @summary 修改分时弹性规则
        
        @param request: ModifyElasticRuleRequest
        @return: ModifyElasticRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_rule_with_options_async(request, runtime)

    def modify_security_iplist_with_options(
        self,
        request: selectdb_20230522_models.ModifySecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the IP addresses in a whitelist of an ApsaraDB for SelectDB instance.
        
        @param request: ModifySecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifySecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_iplist_with_options_async(
        self,
        request: selectdb_20230522_models.ModifySecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the IP addresses in a whitelist of an ApsaraDB for SelectDB instance.
        
        @param request: ModifySecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ModifySecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_iplist(
        self,
        request: selectdb_20230522_models.ModifySecurityIPListRequest,
    ) -> selectdb_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the IP addresses in a whitelist of an ApsaraDB for SelectDB instance.
        
        @param request: ModifySecurityIPListRequest
        @return: ModifySecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_iplist_with_options(request, runtime)

    async def modify_security_iplist_async(
        self,
        request: selectdb_20230522_models.ModifySecurityIPListRequest,
    ) -> selectdb_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the IP addresses in a whitelist of an ApsaraDB for SelectDB instance.
        
        @param request: ModifySecurityIPListRequest
        @return: ModifySecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_iplist_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: selectdb_20230522_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for SelectDB instance.
        
        @param request: ReleaseInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: selectdb_20230522_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for SelectDB instance.
        
        @param request: ReleaseInstancePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancePublicConnectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstancePublicConnection',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: selectdb_20230522_models.ReleaseInstancePublicConnectionRequest,
    ) -> selectdb_20230522_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for SelectDB instance.
        
        @param request: ReleaseInstancePublicConnectionRequest
        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: selectdb_20230522_models.ReleaseInstancePublicConnectionRequest,
    ) -> selectdb_20230522_models.ReleaseInstancePublicConnectionResponse:
        """
        @summary Releases the public endpoint of an ApsaraDB for SelectDB instance.
        
        @param request: ReleaseInstancePublicConnectionRequest
        @return: ReleaseInstancePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: selectdb_20230522_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for SelectDB instance.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: selectdb_20230522_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for SelectDB instance.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: selectdb_20230522_models.ResetAccountPasswordRequest,
    ) -> selectdb_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for SelectDB instance.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: selectdb_20230522_models.ResetAccountPasswordRequest,
    ) -> selectdb_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of an account for an ApsaraDB for SelectDB instance.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbcluster_with_options(
        self,
        request: selectdb_20230522_models.RestartDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.RestartDBClusterResponse:
        """
        @summary Restarts a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: RestartDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.RestartDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbcluster_with_options_async(
        self,
        request: selectdb_20230522_models.RestartDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.RestartDBClusterResponse:
        """
        @summary Restarts a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: RestartDBClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartDBCluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.RestartDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbcluster(
        self,
        request: selectdb_20230522_models.RestartDBClusterRequest,
    ) -> selectdb_20230522_models.RestartDBClusterResponse:
        """
        @summary Restarts a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: RestartDBClusterRequest
        @return: RestartDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbcluster_with_options(request, runtime)

    async def restart_dbcluster_async(
        self,
        request: selectdb_20230522_models.RestartDBClusterRequest,
    ) -> selectdb_20230522_models.RestartDBClusterResponse:
        """
        @summary Restarts a cluster in an ApsaraDB for SelectDB instance.
        
        @param request: RestartDBClusterRequest
        @return: RestartDBClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbcluster_with_options_async(request, runtime)

    def start_becluster_with_options(
        self,
        request: selectdb_20230522_models.StartBEClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.StartBEClusterResponse:
        """
        @summary 暂停后恢复集群
        
        @param request: StartBEClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBEClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBECluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.StartBEClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_becluster_with_options_async(
        self,
        request: selectdb_20230522_models.StartBEClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.StartBEClusterResponse:
        """
        @summary 暂停后恢复集群
        
        @param request: StartBEClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBEClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBECluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.StartBEClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_becluster(
        self,
        request: selectdb_20230522_models.StartBEClusterRequest,
    ) -> selectdb_20230522_models.StartBEClusterResponse:
        """
        @summary 暂停后恢复集群
        
        @param request: StartBEClusterRequest
        @return: StartBEClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_becluster_with_options(request, runtime)

    async def start_becluster_async(
        self,
        request: selectdb_20230522_models.StartBEClusterRequest,
    ) -> selectdb_20230522_models.StartBEClusterResponse:
        """
        @summary 暂停后恢复集群
        
        @param request: StartBEClusterRequest
        @return: StartBEClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_becluster_with_options_async(request, runtime)

    def stop_becluster_with_options(
        self,
        request: selectdb_20230522_models.StopBEClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.StopBEClusterResponse:
        """
        @summary 暂停BE集群
        
        @param request: StopBEClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopBEClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopBECluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.StopBEClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_becluster_with_options_async(
        self,
        request: selectdb_20230522_models.StopBEClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.StopBEClusterResponse:
        """
        @summary 暂停BE集群
        
        @param request: StopBEClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopBEClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopBECluster',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.StopBEClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_becluster(
        self,
        request: selectdb_20230522_models.StopBEClusterRequest,
    ) -> selectdb_20230522_models.StopBEClusterResponse:
        """
        @summary 暂停BE集群
        
        @param request: StopBEClusterRequest
        @return: StopBEClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_becluster_with_options(request, runtime)

    async def stop_becluster_async(
        self,
        request: selectdb_20230522_models.StopBEClusterRequest,
    ) -> selectdb_20230522_models.StopBEClusterResponse:
        """
        @summary 暂停BE集群
        
        @param request: StopBEClusterRequest
        @return: StopBEClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_becluster_with_options_async(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(
        self,
        request: selectdb_20230522_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Updates the database engine version of an ApsaraDB for SelectDB instance.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.UpgradeDBInstanceEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_engine_version_with_options_async(
        self,
        request: selectdb_20230522_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> selectdb_20230522_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Updates the database engine version of an ApsaraDB for SelectDB instance.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeDBInstanceEngineVersion',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            selectdb_20230522_models.UpgradeDBInstanceEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_engine_version(
        self,
        request: selectdb_20230522_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> selectdb_20230522_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Updates the database engine version of an ApsaraDB for SelectDB instance.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    async def upgrade_dbinstance_engine_version_async(
        self,
        request: selectdb_20230522_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> selectdb_20230522_models.UpgradeDBInstanceEngineVersionResponse:
        """
        @summary Updates the database engine version of an ApsaraDB for SelectDB instance.
        
        @param request: UpgradeDBInstanceEngineVersionRequest
        @return: UpgradeDBInstanceEngineVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_engine_version_with_options_async(request, runtime)
