# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cddc20200320 import models as cddc_20200320_models
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
        self._endpoint = self.get_endpoint('cddc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_prins_instance_with_options(
        self,
        tmp_req: cddc_20200320_models.AddPrinsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AddPrinsInstanceResponse:
        """
        @summary 纳管实例
        
        @param tmp_req: AddPrinsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPrinsInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.AddPrinsInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disk):
            request.disk_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.disk, 'Disk', 'json')
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_shrink):
            query['Disk'] = request.disk_shrink
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrinsInstance',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.AddPrinsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prins_instance_with_options_async(
        self,
        tmp_req: cddc_20200320_models.AddPrinsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AddPrinsInstanceResponse:
        """
        @summary 纳管实例
        
        @param tmp_req: AddPrinsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPrinsInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.AddPrinsInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disk):
            request.disk_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.disk, 'Disk', 'json')
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_shrink):
            query['Disk'] = request.disk_shrink
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrinsInstance',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.AddPrinsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prins_instance(
        self,
        request: cddc_20200320_models.AddPrinsInstanceRequest,
    ) -> cddc_20200320_models.AddPrinsInstanceResponse:
        """
        @summary 纳管实例
        
        @param request: AddPrinsInstanceRequest
        @return: AddPrinsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_prins_instance_with_options(request, runtime)

    async def add_prins_instance_async(
        self,
        request: cddc_20200320_models.AddPrinsInstanceRequest,
    ) -> cddc_20200320_models.AddPrinsInstanceResponse:
        """
        @summary 纳管实例
        
        @param request: AddPrinsInstanceRequest
        @return: AddPrinsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_prins_instance_with_options_async(request, runtime)

    def create_dedicated_host_with_options(
        self,
        tmp_req: cddc_20200320_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        """
        @summary Creates hosts in a dedicated cluster.
        
        @param tmp_req: CreateDedicatedHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedHostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.CreateDedicatedHostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_services):
            request.cluster_services_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_services, 'ClusterServices', 'simple')
        if not UtilClient.is_unset(tmp_req.my_base_ecs_class):
            request.my_base_ecs_class_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.my_base_ecs_class, 'MyBaseEcsClass', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_alias):
            query['ClusterAlias'] = request.cluster_alias
        if not UtilClient.is_unset(request.cluster_services_shrink):
            query['ClusterServices'] = request.cluster_services_shrink
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.host_class):
            query['HostClass'] = request.host_class
        if not UtilClient.is_unset(request.host_storage):
            query['HostStorage'] = request.host_storage
        if not UtilClient.is_unset(request.host_storage_type):
            query['HostStorageType'] = request.host_storage_type
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.my_base_ecs_class_shrink):
            query['MyBaseEcsClass'] = request.my_base_ecs_class_shrink
        if not UtilClient.is_unset(request.os_password):
            query['OsPassword'] = request.os_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcID'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHost',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_with_options_async(
        self,
        tmp_req: cddc_20200320_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        """
        @summary Creates hosts in a dedicated cluster.
        
        @param tmp_req: CreateDedicatedHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedHostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.CreateDedicatedHostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_services):
            request.cluster_services_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_services, 'ClusterServices', 'simple')
        if not UtilClient.is_unset(tmp_req.my_base_ecs_class):
            request.my_base_ecs_class_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.my_base_ecs_class, 'MyBaseEcsClass', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_alias):
            query['ClusterAlias'] = request.cluster_alias
        if not UtilClient.is_unset(request.cluster_services_shrink):
            query['ClusterServices'] = request.cluster_services_shrink
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.host_class):
            query['HostClass'] = request.host_class
        if not UtilClient.is_unset(request.host_storage):
            query['HostStorage'] = request.host_storage
        if not UtilClient.is_unset(request.host_storage_type):
            query['HostStorageType'] = request.host_storage_type
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.my_base_ecs_class_shrink):
            query['MyBaseEcsClass'] = request.my_base_ecs_class_shrink
        if not UtilClient.is_unset(request.os_password):
            query['OsPassword'] = request.os_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcID'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHost',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        """
        @summary Creates hosts in a dedicated cluster.
        
        @param request: CreateDedicatedHostRequest
        @return: CreateDedicatedHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    async def create_dedicated_host_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        """
        @summary Creates hosts in a dedicated cluster.
        
        @param request: CreateDedicatedHostRequest
        @return: CreateDedicatedHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_with_options_async(request, runtime)

    def create_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        """
        @summary Creates an account for a host.
        
        @description Each host can have only one account. Before you create an account for a host, make sure that the existing account of the host is deleted. For more information, see [Create an account for a host](https://help.aliyun.com/document_detail/211413.html).
        
        @param request: CreateDedicatedHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.bastion_instance_id):
            query['BastionInstanceId'] = request.bastion_instance_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='CreateDedicatedHostAccount',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_account_with_options_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        """
        @summary Creates an account for a host.
        
        @description Each host can have only one account. Before you create an account for a host, make sure that the existing account of the host is deleted. For more information, see [Create an account for a host](https://help.aliyun.com/document_detail/211413.html).
        
        @param request: CreateDedicatedHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.bastion_instance_id):
            query['BastionInstanceId'] = request.bastion_instance_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='CreateDedicatedHostAccount',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host_account(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        """
        @summary Creates an account for a host.
        
        @description Each host can have only one account. Before you create an account for a host, make sure that the existing account of the host is deleted. For more information, see [Create an account for a host](https://help.aliyun.com/document_detail/211413.html).
        
        @param request: CreateDedicatedHostAccountRequest
        @return: CreateDedicatedHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    async def create_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        """
        @summary Creates an account for a host.
        
        @description Each host can have only one account. Before you create an account for a host, make sure that the existing account of the host is deleted. For more information, see [Create an account for a host](https://help.aliyun.com/document_detail/211413.html).
        
        @param request: CreateDedicatedHostAccountRequest
        @return: CreateDedicatedHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_account_with_options_async(request, runtime)

    def create_dedicated_host_group_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        """
        @summary Creates a dedicated cluster.
        
        @param request: CreateDedicatedHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedHostGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_policy):
            query['AllocationPolicy'] = request.allocation_policy
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu_allocation_ratio):
            query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        if not UtilClient.is_unset(request.dedicated_host_group_desc):
            query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        if not UtilClient.is_unset(request.disk_allocation_ratio):
            query['DiskAllocationRatio'] = request.disk_allocation_ratio
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.host_replace_policy):
            query['HostReplacePolicy'] = request.host_replace_policy
        if not UtilClient.is_unset(request.mem_allocation_ratio):
            query['MemAllocationRatio'] = request.mem_allocation_ratio
        if not UtilClient.is_unset(request.open_permission):
            query['OpenPermission'] = request.open_permission
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostGroup',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_host_group_with_options_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        """
        @summary Creates a dedicated cluster.
        
        @param request: CreateDedicatedHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedHostGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_policy):
            query['AllocationPolicy'] = request.allocation_policy
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu_allocation_ratio):
            query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        if not UtilClient.is_unset(request.dedicated_host_group_desc):
            query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        if not UtilClient.is_unset(request.disk_allocation_ratio):
            query['DiskAllocationRatio'] = request.disk_allocation_ratio
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.host_replace_policy):
            query['HostReplacePolicy'] = request.host_replace_policy
        if not UtilClient.is_unset(request.mem_allocation_ratio):
            query['MemAllocationRatio'] = request.mem_allocation_ratio
        if not UtilClient.is_unset(request.open_permission):
            query['OpenPermission'] = request.open_permission
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDedicatedHostGroup',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_host_group(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        """
        @summary Creates a dedicated cluster.
        
        @param request: CreateDedicatedHostGroupRequest
        @return: CreateDedicatedHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    async def create_dedicated_host_group_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        """
        @summary Creates a dedicated cluster.
        
        @param request: CreateDedicatedHostGroupRequest
        @return: CreateDedicatedHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_group_with_options_async(request, runtime)

    def create_my_base_with_options(
        self,
        tmp_req: cddc_20200320_models.CreateMyBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateMyBaseResponse:
        """
        @summary 创建专属集群（包含主机信息，附加服务信息）
        
        @param tmp_req: CreateMyBaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMyBaseResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.CreateMyBaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ecsclass_list):
            request.ecsclass_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ecsclass_list, 'ECSClassList', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_group_description):
            query['DedicatedHostGroupDescription'] = request.dedicated_host_group_description
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.ecsclass_list_shrink):
            query['ECSClassList'] = request.ecsclass_list_shrink
        if not UtilClient.is_unset(request.ecs_deployment_set_id):
            query['EcsDeploymentSetId'] = request.ecs_deployment_set_id
        if not UtilClient.is_unset(request.ecs_host_name):
            query['EcsHostName'] = request.ecs_host_name
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['EcsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.ecs_unique_suffix):
            query['EcsUniqueSuffix'] = request.ecs_unique_suffix
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.os_password):
            query['OsPassword'] = request.os_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.user_data_in_base_64):
            query['UserDataInBase64'] = request.user_data_in_base_64
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
            action='CreateMyBase',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateMyBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_my_base_with_options_async(
        self,
        tmp_req: cddc_20200320_models.CreateMyBaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateMyBaseResponse:
        """
        @summary 创建专属集群（包含主机信息，附加服务信息）
        
        @param tmp_req: CreateMyBaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMyBaseResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.CreateMyBaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ecsclass_list):
            request.ecsclass_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ecsclass_list, 'ECSClassList', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_host_group_description):
            query['DedicatedHostGroupDescription'] = request.dedicated_host_group_description
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.ecsclass_list_shrink):
            query['ECSClassList'] = request.ecsclass_list_shrink
        if not UtilClient.is_unset(request.ecs_deployment_set_id):
            query['EcsDeploymentSetId'] = request.ecs_deployment_set_id
        if not UtilClient.is_unset(request.ecs_host_name):
            query['EcsHostName'] = request.ecs_host_name
        if not UtilClient.is_unset(request.ecs_instance_name):
            query['EcsInstanceName'] = request.ecs_instance_name
        if not UtilClient.is_unset(request.ecs_unique_suffix):
            query['EcsUniqueSuffix'] = request.ecs_unique_suffix
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.os_password):
            query['OsPassword'] = request.os_password
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.user_data_in_base_64):
            query['UserDataInBase64'] = request.user_data_in_base_64
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
            action='CreateMyBase',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateMyBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_my_base(
        self,
        request: cddc_20200320_models.CreateMyBaseRequest,
    ) -> cddc_20200320_models.CreateMyBaseResponse:
        """
        @summary 创建专属集群（包含主机信息，附加服务信息）
        
        @param request: CreateMyBaseRequest
        @return: CreateMyBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_my_base_with_options(request, runtime)

    async def create_my_base_async(
        self,
        request: cddc_20200320_models.CreateMyBaseRequest,
    ) -> cddc_20200320_models.CreateMyBaseResponse:
        """
        @summary 创建专属集群（包含主机信息，附加服务信息）
        
        @param request: CreateMyBaseRequest
        @return: CreateMyBaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_my_base_with_options_async(request, runtime)

    def create_prins_backup_plan_with_options(
        self,
        request: cddc_20200320_models.CreatePrinsBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreatePrinsBackupPlanResponse:
        """
        @summary 创建备份计划
        
        @param request: CreatePrinsBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrinsBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrinsBackupPlan',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreatePrinsBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prins_backup_plan_with_options_async(
        self,
        request: cddc_20200320_models.CreatePrinsBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreatePrinsBackupPlanResponse:
        """
        @summary 创建备份计划
        
        @param request: CreatePrinsBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrinsBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrinsBackupPlan',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreatePrinsBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prins_backup_plan(
        self,
        request: cddc_20200320_models.CreatePrinsBackupPlanRequest,
    ) -> cddc_20200320_models.CreatePrinsBackupPlanResponse:
        """
        @summary 创建备份计划
        
        @param request: CreatePrinsBackupPlanRequest
        @return: CreatePrinsBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_prins_backup_plan_with_options(request, runtime)

    async def create_prins_backup_plan_async(
        self,
        request: cddc_20200320_models.CreatePrinsBackupPlanRequest,
    ) -> cddc_20200320_models.CreatePrinsBackupPlanResponse:
        """
        @summary 创建备份计划
        
        @param request: CreatePrinsBackupPlanRequest
        @return: CreatePrinsBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_prins_backup_plan_with_options_async(request, runtime)

    def delete_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        """
        @summary Deletes a host account.
        
        @param request: DeleteDedicatedHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDedicatedHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='DeleteDedicatedHostAccount',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dedicated_host_account_with_options_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        """
        @summary Deletes a host account.
        
        @param request: DeleteDedicatedHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDedicatedHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='DeleteDedicatedHostAccount',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dedicated_host_account(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        """
        @summary Deletes a host account.
        
        @param request: DeleteDedicatedHostAccountRequest
        @return: DeleteDedicatedHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    async def delete_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        """
        @summary Deletes a host account.
        
        @param request: DeleteDedicatedHostAccountRequest
        @return: DeleteDedicatedHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_account_with_options_async(request, runtime)

    def delete_dedicated_host_group_with_options(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        """
        @summary Deletes a dedicated cluster.
        
        @description You can call this operation to delete a dedicated cluster only after all the instances and hosts in the dedicated cluster are deleted.
        
        @param request: DeleteDedicatedHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDedicatedHostGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
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
            action='DeleteDedicatedHostGroup',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dedicated_host_group_with_options_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        """
        @summary Deletes a dedicated cluster.
        
        @description You can call this operation to delete a dedicated cluster only after all the instances and hosts in the dedicated cluster are deleted.
        
        @param request: DeleteDedicatedHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDedicatedHostGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
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
            action='DeleteDedicatedHostGroup',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dedicated_host_group(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        """
        @summary Deletes a dedicated cluster.
        
        @description You can call this operation to delete a dedicated cluster only after all the instances and hosts in the dedicated cluster are deleted.
        
        @param request: DeleteDedicatedHostGroupRequest
        @return: DeleteDedicatedHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    async def delete_dedicated_host_group_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        """
        @summary Deletes a dedicated cluster.
        
        @description You can call this operation to delete a dedicated cluster only after all the instances and hosts in the dedicated cluster are deleted.
        
        @param request: DeleteDedicatedHostGroupRequest
        @return: DeleteDedicatedHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_group_with_options_async(request, runtime)

    def describe_dedicated_host_attribute_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        """
        @summary Queries the parameter settings of a host in a dedicated cluster.
        
        @param request: DescribeDedicatedHostAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='DescribeDedicatedHostAttribute',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_attribute_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        """
        @summary Queries the parameter settings of a host in a dedicated cluster.
        
        @param request: DescribeDedicatedHostAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='DescribeDedicatedHostAttribute',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_attribute(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        """
        @summary Queries the parameter settings of a host in a dedicated cluster.
        
        @param request: DescribeDedicatedHostAttributeRequest
        @return: DescribeDedicatedHostAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    async def describe_dedicated_host_attribute_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        """
        @summary Queries the parameter settings of a host in a dedicated cluster.
        
        @param request: DescribeDedicatedHostAttributeRequest
        @return: DescribeDedicatedHostAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_attribute_with_options_async(request, runtime)

    def describe_dedicated_host_disks_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        """
        @summary Queries the information about disks on a host.
        
        @param request: DescribeDedicatedHostDisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostDisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='DescribeDedicatedHostDisks',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_disks_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        """
        @summary Queries the information about disks on a host.
        
        @param request: DescribeDedicatedHostDisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostDisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='DescribeDedicatedHostDisks',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_disks(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        """
        @summary Queries the information about disks on a host.
        
        @param request: DescribeDedicatedHostDisksRequest
        @return: DescribeDedicatedHostDisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_disks_with_options(request, runtime)

    async def describe_dedicated_host_disks_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        """
        @summary Queries the information about disks on a host.
        
        @param request: DescribeDedicatedHostDisksRequest
        @return: DescribeDedicatedHostDisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_disks_with_options_async(request, runtime)

    def describe_dedicated_host_groups_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        """
        @summary Queries the information about hosts in dedicated clusters.
        
        @param request: DescribeDedicatedHostGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
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
            action='DescribeDedicatedHostGroups',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_host_groups_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        """
        @summary Queries the information about hosts in dedicated clusters.
        
        @param request: DescribeDedicatedHostGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
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
            action='DescribeDedicatedHostGroups',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_host_groups(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        """
        @summary Queries the information about hosts in dedicated clusters.
        
        @param request: DescribeDedicatedHostGroupsRequest
        @return: DescribeDedicatedHostGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    async def describe_dedicated_host_groups_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        """
        @summary Queries the information about hosts in dedicated clusters.
        
        @param request: DescribeDedicatedHostGroupsRequest
        @return: DescribeDedicatedHostGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_groups_with_options_async(request, runtime)

    def describe_dedicated_hosts_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        """
        @summary Queries the information about hosts in a dedicated cluster.
        
        @description After hosts are created in a dedicated cluster, you can query the information about the hosts such as performance metrics, total number of CPU cores, total memory size, and total storage.
        
        @param request: DescribeDedicatedHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_status):
            query['AllocationStatus'] = request.allocation_status
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.host_status):
            query['HostStatus'] = request.host_status
        if not UtilClient.is_unset(request.host_type):
            query['HostType'] = request.host_type
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_hosts_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        """
        @summary Queries the information about hosts in a dedicated cluster.
        
        @description After hosts are created in a dedicated cluster, you can query the information about the hosts such as performance metrics, total number of CPU cores, total memory size, and total storage.
        
        @param request: DescribeDedicatedHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedHostsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_status):
            query['AllocationStatus'] = request.allocation_status
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.host_status):
            query['HostStatus'] = request.host_status
        if not UtilClient.is_unset(request.host_type):
            query['HostType'] = request.host_type
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_numbers):
            query['PageNumbers'] = request.page_numbers
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedHosts',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_hosts(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        """
        @summary Queries the information about hosts in a dedicated cluster.
        
        @description After hosts are created in a dedicated cluster, you can query the information about the hosts such as performance metrics, total number of CPU cores, total memory size, and total storage.
        
        @param request: DescribeDedicatedHostsRequest
        @return: DescribeDedicatedHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    async def describe_dedicated_hosts_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        """
        @summary Queries the information about hosts in a dedicated cluster.
        
        @description After hosts are created in a dedicated cluster, you can query the information about the hosts such as performance metrics, total number of CPU cores, total memory size, and total storage.
        
        @param request: DescribeDedicatedHostsRequest
        @return: DescribeDedicatedHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_with_options_async(request, runtime)

    def describe_host_ecs_level_info_with_options(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        """
        @summary Queries the information about host specifications.
        
        @description After a host is created, you can call this operation to query the information about the host specifications, such as the CPU resources, memory resources, CPU model, host category, and storage type.
        
        @param request: DescribeHostEcsLevelInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHostEcsLevelInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHostEcsLevelInfo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostEcsLevelInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_host_ecs_level_info_with_options_async(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        """
        @summary Queries the information about host specifications.
        
        @description After a host is created, you can call this operation to query the information about the host specifications, such as the CPU resources, memory resources, CPU model, host category, and storage type.
        
        @param request: DescribeHostEcsLevelInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHostEcsLevelInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHostEcsLevelInfo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostEcsLevelInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_host_ecs_level_info(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        """
        @summary Queries the information about host specifications.
        
        @description After a host is created, you can call this operation to query the information about the host specifications, such as the CPU resources, memory resources, CPU model, host category, and storage type.
        
        @param request: DescribeHostEcsLevelInfoRequest
        @return: DescribeHostEcsLevelInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_host_ecs_level_info_with_options(request, runtime)

    async def describe_host_ecs_level_info_async(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        """
        @summary Queries the information about host specifications.
        
        @description After a host is created, you can call this operation to query the information about the host specifications, such as the CPU resources, memory resources, CPU model, host category, and storage type.
        
        @param request: DescribeHostEcsLevelInfoRequest
        @return: DescribeHostEcsLevelInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_ecs_level_info_with_options_async(request, runtime)

    def describe_host_web_shell_with_options(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        """
        @summary Queries the URL of a webshell that is used to access a host.
        
        @description You can use a webshell to access a host in an ApsaraDB MyBase for MySQL or ApsaraDB MyBase for PostgreSQL dedicated cluster. For more information, see [Use a webshell to access a host](https://help.aliyun.com/document_detail/205456.html).
        
        @param request: DescribeHostWebShellRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHostWebShellResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeHostWebShell',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostWebShellResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_host_web_shell_with_options_async(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        """
        @summary Queries the URL of a webshell that is used to access a host.
        
        @description You can use a webshell to access a host in an ApsaraDB MyBase for MySQL or ApsaraDB MyBase for PostgreSQL dedicated cluster. For more information, see [Use a webshell to access a host](https://help.aliyun.com/document_detail/205456.html).
        
        @param request: DescribeHostWebShellRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHostWebShellResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
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
            action='DescribeHostWebShell',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostWebShellResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_host_web_shell(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        """
        @summary Queries the URL of a webshell that is used to access a host.
        
        @description You can use a webshell to access a host in an ApsaraDB MyBase for MySQL or ApsaraDB MyBase for PostgreSQL dedicated cluster. For more information, see [Use a webshell to access a host](https://help.aliyun.com/document_detail/205456.html).
        
        @param request: DescribeHostWebShellRequest
        @return: DescribeHostWebShellResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_host_web_shell_with_options(request, runtime)

    async def describe_host_web_shell_async(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        """
        @summary Queries the URL of a webshell that is used to access a host.
        
        @description You can use a webshell to access a host in an ApsaraDB MyBase for MySQL or ApsaraDB MyBase for PostgreSQL dedicated cluster. For more information, see [Use a webshell to access a host](https://help.aliyun.com/document_detail/205456.html).
        
        @param request: DescribeHostWebShellRequest
        @return: DescribeHostWebShellResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_web_shell_with_options_async(request, runtime)

    def describe_prins_backup_plan_with_options(
        self,
        request: cddc_20200320_models.DescribePrinsBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribePrinsBackupPlanResponse:
        """
        @summary 查询备份计划详情
        
        @param request: DescribePrinsBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrinsBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrinsBackupPlan',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribePrinsBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prins_backup_plan_with_options_async(
        self,
        request: cddc_20200320_models.DescribePrinsBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribePrinsBackupPlanResponse:
        """
        @summary 查询备份计划详情
        
        @param request: DescribePrinsBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrinsBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrinsBackupPlan',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribePrinsBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prins_backup_plan(
        self,
        request: cddc_20200320_models.DescribePrinsBackupPlanRequest,
    ) -> cddc_20200320_models.DescribePrinsBackupPlanResponse:
        """
        @summary 查询备份计划详情
        
        @param request: DescribePrinsBackupPlanRequest
        @return: DescribePrinsBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_prins_backup_plan_with_options(request, runtime)

    async def describe_prins_backup_plan_async(
        self,
        request: cddc_20200320_models.DescribePrinsBackupPlanRequest,
    ) -> cddc_20200320_models.DescribePrinsBackupPlanResponse:
        """
        @summary 查询备份计划详情
        
        @param request: DescribePrinsBackupPlanRequest
        @return: DescribePrinsBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_prins_backup_plan_with_options_async(request, runtime)

    def describe_prins_ecs_instances_with_options(
        self,
        request: cddc_20200320_models.DescribePrinsEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribePrinsEcsInstancesResponse:
        """
        @summary 查询ecs实例信息列表
        
        @param request: DescribePrinsEcsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrinsEcsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrinsEcsInstances',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribePrinsEcsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prins_ecs_instances_with_options_async(
        self,
        request: cddc_20200320_models.DescribePrinsEcsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribePrinsEcsInstancesResponse:
        """
        @summary 查询ecs实例信息列表
        
        @param request: DescribePrinsEcsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrinsEcsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrinsEcsInstances',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribePrinsEcsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prins_ecs_instances(
        self,
        request: cddc_20200320_models.DescribePrinsEcsInstancesRequest,
    ) -> cddc_20200320_models.DescribePrinsEcsInstancesResponse:
        """
        @summary 查询ecs实例信息列表
        
        @param request: DescribePrinsEcsInstancesRequest
        @return: DescribePrinsEcsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_prins_ecs_instances_with_options(request, runtime)

    async def describe_prins_ecs_instances_async(
        self,
        request: cddc_20200320_models.DescribePrinsEcsInstancesRequest,
    ) -> cddc_20200320_models.DescribePrinsEcsInstancesResponse:
        """
        @summary 查询ecs实例信息列表
        
        @param request: DescribePrinsEcsInstancesRequest
        @return: DescribePrinsEcsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_prins_ecs_instances_with_options_async(request, runtime)

    def describe_prins_instance_with_options(
        self,
        request: cddc_20200320_models.DescribePrinsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribePrinsInstanceResponse:
        """
        @summary 获取纳管实例详情
        
        @param request: DescribePrinsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrinsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.discover):
            query['Discover'] = request.discover
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrinsInstance',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribePrinsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prins_instance_with_options_async(
        self,
        request: cddc_20200320_models.DescribePrinsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribePrinsInstanceResponse:
        """
        @summary 获取纳管实例详情
        
        @param request: DescribePrinsInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrinsInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.discover):
            query['Discover'] = request.discover
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrinsInstance',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribePrinsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prins_instance(
        self,
        request: cddc_20200320_models.DescribePrinsInstanceRequest,
    ) -> cddc_20200320_models.DescribePrinsInstanceResponse:
        """
        @summary 获取纳管实例详情
        
        @param request: DescribePrinsInstanceRequest
        @return: DescribePrinsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_prins_instance_with_options(request, runtime)

    async def describe_prins_instance_async(
        self,
        request: cddc_20200320_models.DescribePrinsInstanceRequest,
    ) -> cddc_20200320_models.DescribePrinsInstanceResponse:
        """
        @summary 获取纳管实例详情
        
        @param request: DescribePrinsInstanceRequest
        @return: DescribePrinsInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_prins_instance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list.
        
        @description For more information about region IDs, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list.
        
        @description For more information about region IDs, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list.
        
        @description For more information about region IDs, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        """
        @summary Queries the most recent region list.
        
        @description For more information about region IDs, see [Region IDs](https://help.aliyun.com/document_detail/198326.html).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def get_prins_event_list_with_options(
        self,
        request: cddc_20200320_models.GetPrinsEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.GetPrinsEventListResponse:
        """
        @summary 获取事件列表
        
        @param request: GetPrinsEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrinsEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrinsEventList',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.GetPrinsEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prins_event_list_with_options_async(
        self,
        request: cddc_20200320_models.GetPrinsEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.GetPrinsEventListResponse:
        """
        @summary 获取事件列表
        
        @param request: GetPrinsEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrinsEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrinsEventList',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.GetPrinsEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prins_event_list(
        self,
        request: cddc_20200320_models.GetPrinsEventListRequest,
    ) -> cddc_20200320_models.GetPrinsEventListResponse:
        """
        @summary 获取事件列表
        
        @param request: GetPrinsEventListRequest
        @return: GetPrinsEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_prins_event_list_with_options(request, runtime)

    async def get_prins_event_list_async(
        self,
        request: cddc_20200320_models.GetPrinsEventListRequest,
    ) -> cddc_20200320_models.GetPrinsEventListResponse:
        """
        @summary 获取事件列表
        
        @param request: GetPrinsEventListRequest
        @return: GetPrinsEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_prins_event_list_with_options_async(request, runtime)

    def get_prins_metrics_list_with_options(
        self,
        request: cddc_20200320_models.GetPrinsMetricsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.GetPrinsMetricsListResponse:
        """
        @summary 获取纳管实例性能指标数据
        
        @param request: GetPrinsMetricsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrinsMetricsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrinsMetricsList',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.GetPrinsMetricsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prins_metrics_list_with_options_async(
        self,
        request: cddc_20200320_models.GetPrinsMetricsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.GetPrinsMetricsListResponse:
        """
        @summary 获取纳管实例性能指标数据
        
        @param request: GetPrinsMetricsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrinsMetricsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrinsMetricsList',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.GetPrinsMetricsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prins_metrics_list(
        self,
        request: cddc_20200320_models.GetPrinsMetricsListRequest,
    ) -> cddc_20200320_models.GetPrinsMetricsListResponse:
        """
        @summary 获取纳管实例性能指标数据
        
        @param request: GetPrinsMetricsListRequest
        @return: GetPrinsMetricsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_prins_metrics_list_with_options(request, runtime)

    async def get_prins_metrics_list_async(
        self,
        request: cddc_20200320_models.GetPrinsMetricsListRequest,
    ) -> cddc_20200320_models.GetPrinsMetricsListResponse:
        """
        @summary 获取纳管实例性能指标数据
        
        @param request: GetPrinsMetricsListRequest
        @return: GetPrinsMetricsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_prins_metrics_list_with_options_async(request, runtime)

    def list_prins_instances_with_options(
        self,
        tmp_req: cddc_20200320_models.ListPrinsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListPrinsInstancesResponse:
        """
        @summary 列举纳管实例列表
        
        @param tmp_req: ListPrinsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrinsInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.ListPrinsInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrinsInstances',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListPrinsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prins_instances_with_options_async(
        self,
        tmp_req: cddc_20200320_models.ListPrinsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListPrinsInstancesResponse:
        """
        @summary 列举纳管实例列表
        
        @param tmp_req: ListPrinsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrinsInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cddc_20200320_models.ListPrinsInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrinsInstances',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListPrinsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prins_instances(
        self,
        request: cddc_20200320_models.ListPrinsInstancesRequest,
    ) -> cddc_20200320_models.ListPrinsInstancesResponse:
        """
        @summary 列举纳管实例列表
        
        @param request: ListPrinsInstancesRequest
        @return: ListPrinsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_prins_instances_with_options(request, runtime)

    async def list_prins_instances_async(
        self,
        request: cddc_20200320_models.ListPrinsInstancesRequest,
    ) -> cddc_20200320_models.ListPrinsInstancesResponse:
        """
        @summary 列举纳管实例列表
        
        @param request: ListPrinsInstancesRequest
        @return: ListPrinsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_prins_instances_with_options_async(request, runtime)

    def list_prins_params_with_options(
        self,
        request: cddc_20200320_models.ListPrinsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListPrinsParamsResponse:
        """
        @summary 查询数据库纳管实例参数列表
        
        @param request: ListPrinsParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrinsParamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
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
            action='ListPrinsParams',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListPrinsParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prins_params_with_options_async(
        self,
        request: cddc_20200320_models.ListPrinsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListPrinsParamsResponse:
        """
        @summary 查询数据库纳管实例参数列表
        
        @param request: ListPrinsParamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrinsParamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
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
            action='ListPrinsParams',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListPrinsParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prins_params(
        self,
        request: cddc_20200320_models.ListPrinsParamsRequest,
    ) -> cddc_20200320_models.ListPrinsParamsResponse:
        """
        @summary 查询数据库纳管实例参数列表
        
        @param request: ListPrinsParamsRequest
        @return: ListPrinsParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_prins_params_with_options(request, runtime)

    async def list_prins_params_async(
        self,
        request: cddc_20200320_models.ListPrinsParamsRequest,
    ) -> cddc_20200320_models.ListPrinsParamsResponse:
        """
        @summary 查询数据库纳管实例参数列表
        
        @param request: ListPrinsParamsRequest
        @return: ListPrinsParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_prins_params_with_options_async(request, runtime)

    def list_prins_sqlerror_log_with_options(
        self,
        request: cddc_20200320_models.ListPrinsSQLErrorLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListPrinsSQLErrorLogResponse:
        """
        @summary 查询数据库错误日志
        
        @param request: ListPrinsSQLErrorLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrinsSQLErrorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.log_path):
            query['LogPath'] = request.log_path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_linenum):
            query['StartLinenum'] = request.start_linenum
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrinsSQLErrorLog',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListPrinsSQLErrorLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prins_sqlerror_log_with_options_async(
        self,
        request: cddc_20200320_models.ListPrinsSQLErrorLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListPrinsSQLErrorLogResponse:
        """
        @summary 查询数据库错误日志
        
        @param request: ListPrinsSQLErrorLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrinsSQLErrorLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.log_path):
            query['LogPath'] = request.log_path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_linenum):
            query['StartLinenum'] = request.start_linenum
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrinsSQLErrorLog',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListPrinsSQLErrorLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prins_sqlerror_log(
        self,
        request: cddc_20200320_models.ListPrinsSQLErrorLogRequest,
    ) -> cddc_20200320_models.ListPrinsSQLErrorLogResponse:
        """
        @summary 查询数据库错误日志
        
        @param request: ListPrinsSQLErrorLogRequest
        @return: ListPrinsSQLErrorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_prins_sqlerror_log_with_options(request, runtime)

    async def list_prins_sqlerror_log_async(
        self,
        request: cddc_20200320_models.ListPrinsSQLErrorLogRequest,
    ) -> cddc_20200320_models.ListPrinsSQLErrorLogResponse:
        """
        @summary 查询数据库错误日志
        
        @param request: ListPrinsSQLErrorLogRequest
        @return: ListPrinsSQLErrorLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_prins_sqlerror_log_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: cddc_20200320_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListTagResourcesResponse:
        """
        @summary Queries the information about tags that are added to hosts.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: cddc_20200320_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListTagResourcesResponse:
        """
        @summary Queries the information about tags that are added to hosts.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: cddc_20200320_models.ListTagResourcesRequest,
    ) -> cddc_20200320_models.ListTagResourcesResponse:
        """
        @summary Queries the information about tags that are added to hosts.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cddc_20200320_models.ListTagResourcesRequest,
    ) -> cddc_20200320_models.ListTagResourcesResponse:
        """
        @summary Queries the information about tags that are added to hosts.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        """
        @summary Changes the account name and password of a host.
        
        @param request: ModifyDedicatedHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='ModifyDedicatedHostAccount',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_account_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        """
        @summary Changes the account name and password of a host.
        
        @param request: ModifyDedicatedHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='ModifyDedicatedHostAccount',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_account(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        """
        @summary Changes the account name and password of a host.
        
        @param request: ModifyDedicatedHostAccountRequest
        @return: ModifyDedicatedHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    async def modify_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        """
        @summary Changes the account name and password of a host.
        
        @param request: ModifyDedicatedHostAccountRequest
        @return: ModifyDedicatedHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_account_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        """
        @summary Specifies whether instances can be deployed on a host in a dedicated cluster.
        
        @param request: ModifyDedicatedHostAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_status):
            query['AllocationStatus'] = request.allocation_status
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
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
            action='ModifyDedicatedHostAttribute',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_attribute_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        """
        @summary Specifies whether instances can be deployed on a host in a dedicated cluster.
        
        @param request: ModifyDedicatedHostAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_status):
            query['AllocationStatus'] = request.allocation_status
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
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
            action='ModifyDedicatedHostAttribute',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_attribute(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        """
        @summary Specifies whether instances can be deployed on a host in a dedicated cluster.
        
        @param request: ModifyDedicatedHostAttributeRequest
        @return: ModifyDedicatedHostAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        """
        @summary Specifies whether instances can be deployed on a host in a dedicated cluster.
        
        @param request: ModifyDedicatedHostAttributeRequest
        @return: ModifyDedicatedHostAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_class_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        """
        @summary Upgrades host specifications.
        
        @description After a host is created in a dedicated cluster, you can modify the specifications of the host based on your business requirements. The host specifications include the CPU and memory resources. For more information, see [Upgrade host specifications](https://help.aliyun.com/document_detail/262822.html).
        >  When you upgrade the specifications of a host, the host restarts. The database instances that are running on the host also restart. For information about the impacts of a host restart, see [Restart a host](https://help.aliyun.com/document_detail/141772.html).
        
        @param request: ModifyDedicatedHostClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_class_code):
            query['TargetClassCode'] = request.target_class_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostClass',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_class_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        """
        @summary Upgrades host specifications.
        
        @description After a host is created in a dedicated cluster, you can modify the specifications of the host based on your business requirements. The host specifications include the CPU and memory resources. For more information, see [Upgrade host specifications](https://help.aliyun.com/document_detail/262822.html).
        >  When you upgrade the specifications of a host, the host restarts. The database instances that are running on the host also restart. For information about the impacts of a host restart, see [Restart a host](https://help.aliyun.com/document_detail/141772.html).
        
        @param request: ModifyDedicatedHostClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_class_code):
            query['TargetClassCode'] = request.target_class_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedHostClass',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_class(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        """
        @summary Upgrades host specifications.
        
        @description After a host is created in a dedicated cluster, you can modify the specifications of the host based on your business requirements. The host specifications include the CPU and memory resources. For more information, see [Upgrade host specifications](https://help.aliyun.com/document_detail/262822.html).
        >  When you upgrade the specifications of a host, the host restarts. The database instances that are running on the host also restart. For information about the impacts of a host restart, see [Restart a host](https://help.aliyun.com/document_detail/141772.html).
        
        @param request: ModifyDedicatedHostClassRequest
        @return: ModifyDedicatedHostClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_class_with_options(request, runtime)

    async def modify_dedicated_host_class_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        """
        @summary Upgrades host specifications.
        
        @description After a host is created in a dedicated cluster, you can modify the specifications of the host based on your business requirements. The host specifications include the CPU and memory resources. For more information, see [Upgrade host specifications](https://help.aliyun.com/document_detail/262822.html).
        >  When you upgrade the specifications of a host, the host restarts. The database instances that are running on the host also restart. For information about the impacts of a host restart, see [Restart a host](https://help.aliyun.com/document_detail/141772.html).
        
        @param request: ModifyDedicatedHostClassRequest
        @return: ModifyDedicatedHostClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_class_with_options_async(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        """
        @summary Modifies configurations such as the CPU overcommit ratio, memory usage, storage overcommit ratio, and resource allocation policy for a dedicated cluster.
        
        @description For more information, see [Manage dedicated clusters](https://help.aliyun.com/document_detail/182328.html).
        
        @param request: ModifyDedicatedHostGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_policy):
            query['AllocationPolicy'] = request.allocation_policy
        if not UtilClient.is_unset(request.cpu_allocation_ratio):
            query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        if not UtilClient.is_unset(request.dedicated_host_group_desc):
            query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.disk_allocation_ratio):
            query['DiskAllocationRatio'] = request.disk_allocation_ratio
        if not UtilClient.is_unset(request.host_replace_policy):
            query['HostReplacePolicy'] = request.host_replace_policy
        if not UtilClient.is_unset(request.mem_allocation_ratio):
            query['MemAllocationRatio'] = request.mem_allocation_ratio
        if not UtilClient.is_unset(request.open_permission):
            query['OpenPermission'] = request.open_permission
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
            action='ModifyDedicatedHostGroupAttribute',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_group_attribute_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        """
        @summary Modifies configurations such as the CPU overcommit ratio, memory usage, storage overcommit ratio, and resource allocation policy for a dedicated cluster.
        
        @description For more information, see [Manage dedicated clusters](https://help.aliyun.com/document_detail/182328.html).
        
        @param request: ModifyDedicatedHostGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_policy):
            query['AllocationPolicy'] = request.allocation_policy
        if not UtilClient.is_unset(request.cpu_allocation_ratio):
            query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        if not UtilClient.is_unset(request.dedicated_host_group_desc):
            query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        if not UtilClient.is_unset(request.dedicated_host_group_id):
            query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        if not UtilClient.is_unset(request.disk_allocation_ratio):
            query['DiskAllocationRatio'] = request.disk_allocation_ratio
        if not UtilClient.is_unset(request.host_replace_policy):
            query['HostReplacePolicy'] = request.host_replace_policy
        if not UtilClient.is_unset(request.mem_allocation_ratio):
            query['MemAllocationRatio'] = request.mem_allocation_ratio
        if not UtilClient.is_unset(request.open_permission):
            query['OpenPermission'] = request.open_permission
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
            action='ModifyDedicatedHostGroupAttribute',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_group_attribute(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        """
        @summary Modifies configurations such as the CPU overcommit ratio, memory usage, storage overcommit ratio, and resource allocation policy for a dedicated cluster.
        
        @description For more information, see [Manage dedicated clusters](https://help.aliyun.com/document_detail/182328.html).
        
        @param request: ModifyDedicatedHostGroupAttributeRequest
        @return: ModifyDedicatedHostGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    async def modify_dedicated_host_group_attribute_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        """
        @summary Modifies configurations such as the CPU overcommit ratio, memory usage, storage overcommit ratio, and resource allocation policy for a dedicated cluster.
        
        @description For more information, see [Manage dedicated clusters](https://help.aliyun.com/document_detail/182328.html).
        
        @param request: ModifyDedicatedHostGroupAttributeRequest
        @return: ModifyDedicatedHostGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_group_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_password_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        """
        @summary Changes the root account password of a host.
        
        @description This operation is supported only for ApsaraDB MyBase for Redis Enhanced Edition (Tair) dedicated clusters.
        
        @param request: ModifyDedicatedHostPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
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
            action='ModifyDedicatedHostPassword',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_host_password_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        """
        @summary Changes the root account password of a host.
        
        @description This operation is supported only for ApsaraDB MyBase for Redis Enhanced Edition (Tair) dedicated clusters.
        
        @param request: ModifyDedicatedHostPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedHostPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.new_password):
            query['NewPassword'] = request.new_password
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
            action='ModifyDedicatedHostPassword',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_host_password(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        """
        @summary Changes the root account password of a host.
        
        @description This operation is supported only for ApsaraDB MyBase for Redis Enhanced Edition (Tair) dedicated clusters.
        
        @param request: ModifyDedicatedHostPasswordRequest
        @return: ModifyDedicatedHostPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_password_with_options(request, runtime)

    async def modify_dedicated_host_password_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        """
        @summary Changes the root account password of a host.
        
        @description This operation is supported only for ApsaraDB MyBase for Redis Enhanced Edition (Tair) dedicated clusters.
        
        @param request: ModifyDedicatedHostPasswordRequest
        @return: ModifyDedicatedHostPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_password_with_options_async(request, runtime)

    def query_host_base_info_by_instance_with_options(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        """
        @summary Queries the basic information about the host on which an instance is deployed.
        
        @param request: QueryHostBaseInfoByInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHostBaseInfoByInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='QueryHostBaseInfoByInstance',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostBaseInfoByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_host_base_info_by_instance_with_options_async(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        """
        @summary Queries the basic information about the host on which an instance is deployed.
        
        @param request: QueryHostBaseInfoByInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHostBaseInfoByInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action='QueryHostBaseInfoByInstance',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostBaseInfoByInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_host_base_info_by_instance(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        """
        @summary Queries the basic information about the host on which an instance is deployed.
        
        @param request: QueryHostBaseInfoByInstanceRequest
        @return: QueryHostBaseInfoByInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_host_base_info_by_instance_with_options(request, runtime)

    async def query_host_base_info_by_instance_async(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        """
        @summary Queries the basic information about the host on which an instance is deployed.
        
        @param request: QueryHostBaseInfoByInstanceRequest
        @return: QueryHostBaseInfoByInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_host_base_info_by_instance_with_options_async(request, runtime)

    def query_host_instance_console_info_with_options(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        """
        @summary Queries the information about instances that are deployed on a host.
        
        @param request: QueryHostInstanceConsoleInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHostInstanceConsoleInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='QueryHostInstanceConsoleInfo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostInstanceConsoleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_host_instance_console_info_with_options_async(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        """
        @summary Queries the information about instances that are deployed on a host.
        
        @param request: QueryHostInstanceConsoleInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryHostInstanceConsoleInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
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
            action='QueryHostInstanceConsoleInfo',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostInstanceConsoleInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_host_instance_console_info(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        """
        @summary Queries the information about instances that are deployed on a host.
        
        @param request: QueryHostInstanceConsoleInfoRequest
        @return: QueryHostInstanceConsoleInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_host_instance_console_info_with_options(request, runtime)

    async def query_host_instance_console_info_async(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        """
        @summary Queries the information about instances that are deployed on a host.
        
        @param request: QueryHostInstanceConsoleInfoRequest
        @return: QueryHostInstanceConsoleInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_host_instance_console_info_with_options_async(request, runtime)

    def replace_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        """
        @summary Replaces a host in a dedicated cluster.
        
        @description If you specify the manual host replacement policy when you create an ApsaraDB MyBase for MySQL dedicated cluster, you can call this operation to replace a *faulty** host in the dedicated cluster.
        >  You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the value of the *HostStatus** parameter.
        
        @param request: ReplaceDedicatedHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceDedicatedHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.failover_mode):
            query['FailoverMode'] = request.failover_mode
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
            action='ReplaceDedicatedHost',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ReplaceDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_dedicated_host_with_options_async(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        """
        @summary Replaces a host in a dedicated cluster.
        
        @description If you specify the manual host replacement policy when you create an ApsaraDB MyBase for MySQL dedicated cluster, you can call this operation to replace a *faulty** host in the dedicated cluster.
        >  You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the value of the *HostStatus** parameter.
        
        @param request: ReplaceDedicatedHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceDedicatedHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.failover_mode):
            query['FailoverMode'] = request.failover_mode
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
            action='ReplaceDedicatedHost',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.ReplaceDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_dedicated_host(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        """
        @summary Replaces a host in a dedicated cluster.
        
        @description If you specify the manual host replacement policy when you create an ApsaraDB MyBase for MySQL dedicated cluster, you can call this operation to replace a *faulty** host in the dedicated cluster.
        >  You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the value of the *HostStatus** parameter.
        
        @param request: ReplaceDedicatedHostRequest
        @return: ReplaceDedicatedHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    async def replace_dedicated_host_async(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        """
        @summary Replaces a host in a dedicated cluster.
        
        @description If you specify the manual host replacement policy when you create an ApsaraDB MyBase for MySQL dedicated cluster, you can call this operation to replace a *faulty** host in the dedicated cluster.
        >  You can call the [DescribeDedicatedHostAttribute](https://help.aliyun.com/document_detail/213010.html) operation to query the value of the *HostStatus** parameter.
        
        @param request: ReplaceDedicatedHostRequest
        @return: ReplaceDedicatedHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.replace_dedicated_host_with_options_async(request, runtime)

    def restart_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        """
        @summary Restarts a host in a dedicated cluster.
        
        @param request: RestartDedicatedHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDedicatedHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.failover_mode):
            query['FailoverMode'] = request.failover_mode
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
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
            action='RestartDedicatedHost',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.RestartDedicatedHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dedicated_host_with_options_async(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        """
        @summary Restarts a host in a dedicated cluster.
        
        @param request: RestartDedicatedHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDedicatedHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.failover_mode):
            query['FailoverMode'] = request.failover_mode
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
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
            action='RestartDedicatedHost',
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.RestartDedicatedHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dedicated_host(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        """
        @summary Restarts a host in a dedicated cluster.
        
        @param request: RestartDedicatedHostRequest
        @return: RestartDedicatedHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    async def restart_dedicated_host_async(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        """
        @summary Restarts a host in a dedicated cluster.
        
        @param request: RestartDedicatedHostRequest
        @return: RestartDedicatedHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dedicated_host_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cddc_20200320_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.TagResourcesResponse:
        """
        @summary Adds tags to hosts.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cddc_20200320_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.TagResourcesResponse:
        """
        @summary Adds tags to hosts.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: cddc_20200320_models.TagResourcesRequest,
    ) -> cddc_20200320_models.TagResourcesResponse:
        """
        @summary Adds tags to hosts.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cddc_20200320_models.TagResourcesRequest,
    ) -> cddc_20200320_models.TagResourcesResponse:
        """
        @summary Adds tags to hosts.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cddc_20200320_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.UntagResourcesResponse:
        """
        @summary Removes tags from hosts.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cddc_20200320_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.UntagResourcesResponse:
        """
        @summary Removes tags from hosts.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
            version='2020-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cddc_20200320_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: cddc_20200320_models.UntagResourcesRequest,
    ) -> cddc_20200320_models.UntagResourcesResponse:
        """
        @summary Removes tags from hosts.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cddc_20200320_models.UntagResourcesRequest,
    ) -> cddc_20200320_models.UntagResourcesResponse:
        """
        @summary Removes tags from hosts.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
