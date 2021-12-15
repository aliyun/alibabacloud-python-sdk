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

    def create_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoRenew'] = request.auto_renew
        query['ClientToken'] = request.client_token
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['HostClass'] = request.host_class
        query['HostName'] = request.host_name
        query['ImageCategory'] = request.image_category
        query['OsPassword'] = request.os_password
        query['OwnerId'] = request.owner_id
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UsedTime'] = request.used_time
        query['VSwitchId'] = request.v_switch_id
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
        request: cddc_20200320_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutoRenew'] = request.auto_renew
        query['ClientToken'] = request.client_token
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['HostClass'] = request.host_class
        query['HostName'] = request.host_name
        query['ImageCategory'] = request.image_category
        query['OsPassword'] = request.os_password
        query['OwnerId'] = request.owner_id
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UsedTime'] = request.used_time
        query['VSwitchId'] = request.v_switch_id
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
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    async def create_dedicated_host_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_with_options_async(request, runtime)

    def create_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AccountType'] = request.account_type
        query['BastionInstanceId'] = request.bastion_instance_id
        query['ClientToken'] = request.client_token
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AccountType'] = request.account_type
        query['BastionInstanceId'] = request.bastion_instance_id
        query['ClientToken'] = request.client_token
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    async def create_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_account_with_options_async(request, runtime)

    def create_dedicated_host_group_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllocationPolicy'] = request.allocation_policy
        query['ClientToken'] = request.client_token
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['Engine'] = request.engine
        query['HostReplacePolicy'] = request.host_replace_policy
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['OpenPermission'] = request.open_permission
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
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
        UtilClient.validate_model(request)
        query = {}
        query['AllocationPolicy'] = request.allocation_policy
        query['ClientToken'] = request.client_token
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['Engine'] = request.engine
        query['HostReplacePolicy'] = request.host_replace_policy
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['OpenPermission'] = request.open_permission
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    async def create_dedicated_host_group_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_group_with_options_async(request, runtime)

    def delete_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    async def delete_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_account_with_options_async(request, runtime)

    def delete_dedicated_host_group_with_options(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    async def delete_dedicated_host_group_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_group_with_options_async(request, runtime)

    def describe_dedicated_host_attribute_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    async def describe_dedicated_host_attribute_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_attribute_with_options_async(request, runtime)

    def describe_dedicated_host_disks_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_disks_with_options(request, runtime)

    async def describe_dedicated_host_disks_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_disks_with_options_async(request, runtime)

    def describe_dedicated_host_groups_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['Engine'] = request.engine
        query['ImageCategory'] = request.image_category
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['Engine'] = request.engine
        query['ImageCategory'] = request.image_category
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    async def describe_dedicated_host_groups_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_groups_with_options_async(request, runtime)

    def describe_dedicated_hosts_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllocationStatus'] = request.allocation_status
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['HostStatus'] = request.host_status
        query['HostType'] = request.host_type
        query['OrderId'] = request.order_id
        query['OwnerId'] = request.owner_id
        query['PageNumbers'] = request.page_numbers
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tags'] = request.tags
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
        UtilClient.validate_model(request)
        query = {}
        query['AllocationStatus'] = request.allocation_status
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DedicatedHostId'] = request.dedicated_host_id
        query['HostStatus'] = request.host_status
        query['HostType'] = request.host_type
        query['OrderId'] = request.order_id
        query['OwnerId'] = request.owner_id
        query['PageNumbers'] = request.page_numbers
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tags'] = request.tags
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
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    async def describe_dedicated_hosts_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_with_options_async(request, runtime)

    def describe_host_ecs_level_info_with_options(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbType'] = request.db_type
        query['ImageCategory'] = request.image_category
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StorageType'] = request.storage_type
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
        UtilClient.validate_model(request)
        query = {}
        query['DbType'] = request.db_type
        query['ImageCategory'] = request.image_category
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StorageType'] = request.storage_type
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
        runtime = util_models.RuntimeOptions()
        return self.describe_host_ecs_level_info_with_options(request, runtime)

    async def describe_host_ecs_level_info_async(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_ecs_level_info_with_options_async(request, runtime)

    def describe_host_web_shell_with_options(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
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
        runtime = util_models.RuntimeOptions()
        return self.describe_host_web_shell_with_options(request, runtime)

    async def describe_host_web_shell_async(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_web_shell_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: cddc_20200320_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
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
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
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
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cddc_20200320_models.ListTagResourcesRequest,
    ) -> cddc_20200320_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    async def modify_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_account_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllocationStatus'] = request.allocation_status
        query['DedicatedHostId'] = request.dedicated_host_id
        query['HostName'] = request.host_name
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['AllocationStatus'] = request.allocation_status
        query['DedicatedHostId'] = request.dedicated_host_id
        query['HostName'] = request.host_name
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_class_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SwitchTime'] = request.switch_time
        query['SwitchTimeMode'] = request.switch_time_mode
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SwitchTime'] = request.switch_time
        query['SwitchTimeMode'] = request.switch_time_mode
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
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_class_with_options(request, runtime)

    async def modify_dedicated_host_class_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_class_with_options_async(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AllocationPolicy'] = request.allocation_policy
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['HostReplacePolicy'] = request.host_replace_policy
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['OpenPermission'] = request.open_permission
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['AllocationPolicy'] = request.allocation_policy
        query['CpuAllocationRatio'] = request.cpu_allocation_ratio
        query['DedicatedHostGroupDesc'] = request.dedicated_host_group_desc
        query['DedicatedHostGroupId'] = request.dedicated_host_group_id
        query['DiskAllocationRatio'] = request.disk_allocation_ratio
        query['HostReplacePolicy'] = request.host_replace_policy
        query['MemAllocationRatio'] = request.mem_allocation_ratio
        query['OpenPermission'] = request.open_permission
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    async def modify_dedicated_host_group_attribute_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_group_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_password_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['NewPassword'] = request.new_password
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['NewPassword'] = request.new_password
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_password_with_options(request, runtime)

    async def modify_dedicated_host_password_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_password_with_options_async(request, runtime)

    def query_host_base_info_by_instance_with_options(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DBInstanceId'] = request.dbinstance_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.query_host_base_info_by_instance_with_options(request, runtime)

    async def query_host_base_info_by_instance_async(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_host_base_info_by_instance_with_options_async(request, runtime)

    def query_host_instance_console_info_with_options(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.query_host_instance_console_info_with_options(request, runtime)

    async def query_host_instance_console_info_async(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_host_instance_console_info_with_options_async(request, runtime)

    def replace_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    async def replace_dedicated_host_async(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_dedicated_host_with_options_async(request, runtime)

    def restart_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        query['ForceStop'] = request.force_stop
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        UtilClient.validate_model(request)
        query = {}
        query['DedicatedHostId'] = request.dedicated_host_id
        query['FailoverMode'] = request.failover_mode
        query['ForceStop'] = request.force_stop
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
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
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    async def restart_dedicated_host_async(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dedicated_host_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cddc_20200320_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
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
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
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
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cddc_20200320_models.TagResourcesRequest,
    ) -> cddc_20200320_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cddc_20200320_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['All'] = request.all
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
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
        UtilClient.validate_model(request)
        query = {}
        query['All'] = request.all
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceId'] = request.resource_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceType'] = request.resource_type
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
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cddc_20200320_models.UntagResourcesRequest,
    ) -> cddc_20200320_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
