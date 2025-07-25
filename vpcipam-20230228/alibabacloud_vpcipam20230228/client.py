# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vpcipam20230228 import models as vpc_ipam_20230228_models
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
        self._endpoint = self.get_endpoint('vpcipam', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_ipam_pool_cidr_with_options(
        self,
        request: vpc_ipam_20230228_models.AddIpamPoolCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.AddIpamPoolCidrResponse:
        """
        @summary Provisions a CIDR block to an IP Address Manager (IPAM) pool.
        
        @description    Before you provision a CIDR block, make sure that an IPAM pool is created. You can call the **CreateIpamPool** operation to create an IPAM pool.
        If no CIDR block is provisioned to a parent pool, you cannot provision CIDR blocks to its subpools.
        If a CIDR block is provisioned to a parent pool, you can provision CIDR blocks to its subpools and the CIDR blocks must be subsets of the CIDR block provisioned to the parent pool.
        If a CIDR block is provisioned to a parent pool and allocations are created, CIDR blocks provisioned to its subpools cannot overlap with existing allocated CIDR blocks.
        You can provision CIDR blocks to a pool only in the region where the IPAM is hosted.
        CIDR blocks provisioned to an IPAM pool cannot overlap with the CIDR blocks provisioned to other pools in the same scope.
        You can provision at most 50 CIDR blocks to each pool.
        
        @param request: AddIpamPoolCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIpamPoolCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.netmask_length):
            query['NetmaskLength'] = request.netmask_length
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIpamPoolCidr',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.AddIpamPoolCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ipam_pool_cidr_with_options_async(
        self,
        request: vpc_ipam_20230228_models.AddIpamPoolCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.AddIpamPoolCidrResponse:
        """
        @summary Provisions a CIDR block to an IP Address Manager (IPAM) pool.
        
        @description    Before you provision a CIDR block, make sure that an IPAM pool is created. You can call the **CreateIpamPool** operation to create an IPAM pool.
        If no CIDR block is provisioned to a parent pool, you cannot provision CIDR blocks to its subpools.
        If a CIDR block is provisioned to a parent pool, you can provision CIDR blocks to its subpools and the CIDR blocks must be subsets of the CIDR block provisioned to the parent pool.
        If a CIDR block is provisioned to a parent pool and allocations are created, CIDR blocks provisioned to its subpools cannot overlap with existing allocated CIDR blocks.
        You can provision CIDR blocks to a pool only in the region where the IPAM is hosted.
        CIDR blocks provisioned to an IPAM pool cannot overlap with the CIDR blocks provisioned to other pools in the same scope.
        You can provision at most 50 CIDR blocks to each pool.
        
        @param request: AddIpamPoolCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIpamPoolCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.netmask_length):
            query['NetmaskLength'] = request.netmask_length
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIpamPoolCidr',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.AddIpamPoolCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ipam_pool_cidr(
        self,
        request: vpc_ipam_20230228_models.AddIpamPoolCidrRequest,
    ) -> vpc_ipam_20230228_models.AddIpamPoolCidrResponse:
        """
        @summary Provisions a CIDR block to an IP Address Manager (IPAM) pool.
        
        @description    Before you provision a CIDR block, make sure that an IPAM pool is created. You can call the **CreateIpamPool** operation to create an IPAM pool.
        If no CIDR block is provisioned to a parent pool, you cannot provision CIDR blocks to its subpools.
        If a CIDR block is provisioned to a parent pool, you can provision CIDR blocks to its subpools and the CIDR blocks must be subsets of the CIDR block provisioned to the parent pool.
        If a CIDR block is provisioned to a parent pool and allocations are created, CIDR blocks provisioned to its subpools cannot overlap with existing allocated CIDR blocks.
        You can provision CIDR blocks to a pool only in the region where the IPAM is hosted.
        CIDR blocks provisioned to an IPAM pool cannot overlap with the CIDR blocks provisioned to other pools in the same scope.
        You can provision at most 50 CIDR blocks to each pool.
        
        @param request: AddIpamPoolCidrRequest
        @return: AddIpamPoolCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_ipam_pool_cidr_with_options(request, runtime)

    async def add_ipam_pool_cidr_async(
        self,
        request: vpc_ipam_20230228_models.AddIpamPoolCidrRequest,
    ) -> vpc_ipam_20230228_models.AddIpamPoolCidrResponse:
        """
        @summary Provisions a CIDR block to an IP Address Manager (IPAM) pool.
        
        @description    Before you provision a CIDR block, make sure that an IPAM pool is created. You can call the **CreateIpamPool** operation to create an IPAM pool.
        If no CIDR block is provisioned to a parent pool, you cannot provision CIDR blocks to its subpools.
        If a CIDR block is provisioned to a parent pool, you can provision CIDR blocks to its subpools and the CIDR blocks must be subsets of the CIDR block provisioned to the parent pool.
        If a CIDR block is provisioned to a parent pool and allocations are created, CIDR blocks provisioned to its subpools cannot overlap with existing allocated CIDR blocks.
        You can provision CIDR blocks to a pool only in the region where the IPAM is hosted.
        CIDR blocks provisioned to an IPAM pool cannot overlap with the CIDR blocks provisioned to other pools in the same scope.
        You can provision at most 50 CIDR blocks to each pool.
        
        @param request: AddIpamPoolCidrRequest
        @return: AddIpamPoolCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_ipam_pool_cidr_with_options_async(request, runtime)

    def associate_ipam_resource_discovery_with_options(
        self,
        request: vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryResponse:
        """
        @summary Associates resource discovery with an IPAM instance.
        
        @description    The specified resource discovery instance can only be associated with one IPAM instance and associations cannot be duplicated.
        
        @param request: AssociateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
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
            action='AssociateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_ipam_resource_discovery_with_options_async(
        self,
        request: vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryResponse:
        """
        @summary Associates resource discovery with an IPAM instance.
        
        @description    The specified resource discovery instance can only be associated with one IPAM instance and associations cannot be duplicated.
        
        @param request: AssociateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
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
            action='AssociateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_ipam_resource_discovery(
        self,
        request: vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryResponse:
        """
        @summary Associates resource discovery with an IPAM instance.
        
        @description    The specified resource discovery instance can only be associated with one IPAM instance and associations cannot be duplicated.
        
        @param request: AssociateIpamResourceDiscoveryRequest
        @return: AssociateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_ipam_resource_discovery_with_options(request, runtime)

    async def associate_ipam_resource_discovery_async(
        self,
        request: vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.AssociateIpamResourceDiscoveryResponse:
        """
        @summary Associates resource discovery with an IPAM instance.
        
        @description    The specified resource discovery instance can only be associated with one IPAM instance and associations cannot be duplicated.
        
        @param request: AssociateIpamResourceDiscoveryRequest
        @return: AssociateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_ipam_resource_discovery_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: vpc_ipam_20230228_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group of an IPAM resource.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group of an IPAM resource.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: vpc_ipam_20230228_models.ChangeResourceGroupRequest,
    ) -> vpc_ipam_20230228_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group of an IPAM resource.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: vpc_ipam_20230228_models.ChangeResourceGroupRequest,
    ) -> vpc_ipam_20230228_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group of an IPAM resource.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_ipam_with_options(
        self,
        request: vpc_ipam_20230228_models.CreateIpamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamResponse:
        """
        @summary Creates an IP Address Manager (IPAM).
        
        @description - You can create only one IPAM with each Alibaba Cloud account in each region.
        - Only IPv4 IP addresses can be allocated.
        - When you create an IPAM instance:
        - If there is no custom resource discovery in the region, the system creates a default resource discovery associated with the IPAM instance.
        - If there is a custom resource discovery in the region, the system converts it to a default resource discovery and associates it with the IPAM instance.
        
        @param request: CreateIpamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not UtilClient.is_unset(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not UtilClient.is_unset(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpam',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_with_options_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamResponse:
        """
        @summary Creates an IP Address Manager (IPAM).
        
        @description - You can create only one IPAM with each Alibaba Cloud account in each region.
        - Only IPv4 IP addresses can be allocated.
        - When you create an IPAM instance:
        - If there is no custom resource discovery in the region, the system creates a default resource discovery associated with the IPAM instance.
        - If there is a custom resource discovery in the region, the system converts it to a default resource discovery and associates it with the IPAM instance.
        
        @param request: CreateIpamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not UtilClient.is_unset(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not UtilClient.is_unset(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpam',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam(
        self,
        request: vpc_ipam_20230228_models.CreateIpamRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamResponse:
        """
        @summary Creates an IP Address Manager (IPAM).
        
        @description - You can create only one IPAM with each Alibaba Cloud account in each region.
        - Only IPv4 IP addresses can be allocated.
        - When you create an IPAM instance:
        - If there is no custom resource discovery in the region, the system creates a default resource discovery associated with the IPAM instance.
        - If there is a custom resource discovery in the region, the system converts it to a default resource discovery and associates it with the IPAM instance.
        
        @param request: CreateIpamRequest
        @return: CreateIpamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ipam_with_options(request, runtime)

    async def create_ipam_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamResponse:
        """
        @summary Creates an IP Address Manager (IPAM).
        
        @description - You can create only one IPAM with each Alibaba Cloud account in each region.
        - Only IPv4 IP addresses can be allocated.
        - When you create an IPAM instance:
        - If there is no custom resource discovery in the region, the system creates a default resource discovery associated with the IPAM instance.
        - If there is a custom resource discovery in the region, the system converts it to a default resource discovery and associates it with the IPAM instance.
        
        @param request: CreateIpamRequest
        @return: CreateIpamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ipam_with_options_async(request, runtime)

    def create_ipam_pool_with_options(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolResponse:
        """
        @summary Creates an IP Address Manager (IPAM) pool.
        
        @param request: CreateIpamPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not UtilClient.is_unset(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not UtilClient.is_unset(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not UtilClient.is_unset(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamPool',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_pool_with_options_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolResponse:
        """
        @summary Creates an IP Address Manager (IPAM) pool.
        
        @param request: CreateIpamPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not UtilClient.is_unset(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not UtilClient.is_unset(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not UtilClient.is_unset(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamPool',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_pool(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolResponse:
        """
        @summary Creates an IP Address Manager (IPAM) pool.
        
        @param request: CreateIpamPoolRequest
        @return: CreateIpamPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ipam_pool_with_options(request, runtime)

    async def create_ipam_pool_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolResponse:
        """
        @summary Creates an IP Address Manager (IPAM) pool.
        
        @param request: CreateIpamPoolRequest
        @return: CreateIpamPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ipam_pool_with_options_async(request, runtime)

    def create_ipam_pool_allocation_with_options(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolAllocationResponse:
        """
        @summary Reserves a custom CIDR block from an IP Address Manager (IPAM) pool.
        
        @description    Before you reserve a custom CIDR block, make sure that an IPAM pool is created and CIDR blocks are added to the pool. You can call **CreateIpamPool** to create an IPAM pool and call **AddIpamPoolCidr** to add CIDR blocks to the pool.
        When you specify Cidr or CidrMask to reserve a custom CIDR block, the mask must fall within the range specified by the IPAM pool.
        If the IPAM pool has the region attribute, you must reserve a custom CIDR block in the region to which the IPAM pool belongs.
        The custom CIDR block that you want to reserve cannot overlap with existing CIDR blocks created from the IPAM pool.
        
        @param request: CreateIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.cidr_mask):
            query['CidrMask'] = request.cidr_mask
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not UtilClient.is_unset(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_pool_allocation_with_options_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolAllocationResponse:
        """
        @summary Reserves a custom CIDR block from an IP Address Manager (IPAM) pool.
        
        @description    Before you reserve a custom CIDR block, make sure that an IPAM pool is created and CIDR blocks are added to the pool. You can call **CreateIpamPool** to create an IPAM pool and call **AddIpamPoolCidr** to add CIDR blocks to the pool.
        When you specify Cidr or CidrMask to reserve a custom CIDR block, the mask must fall within the range specified by the IPAM pool.
        If the IPAM pool has the region attribute, you must reserve a custom CIDR block in the region to which the IPAM pool belongs.
        The custom CIDR block that you want to reserve cannot overlap with existing CIDR blocks created from the IPAM pool.
        
        @param request: CreateIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.cidr_mask):
            query['CidrMask'] = request.cidr_mask
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not UtilClient.is_unset(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_pool_allocation(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolAllocationResponse:
        """
        @summary Reserves a custom CIDR block from an IP Address Manager (IPAM) pool.
        
        @description    Before you reserve a custom CIDR block, make sure that an IPAM pool is created and CIDR blocks are added to the pool. You can call **CreateIpamPool** to create an IPAM pool and call **AddIpamPoolCidr** to add CIDR blocks to the pool.
        When you specify Cidr or CidrMask to reserve a custom CIDR block, the mask must fall within the range specified by the IPAM pool.
        If the IPAM pool has the region attribute, you must reserve a custom CIDR block in the region to which the IPAM pool belongs.
        The custom CIDR block that you want to reserve cannot overlap with existing CIDR blocks created from the IPAM pool.
        
        @param request: CreateIpamPoolAllocationRequest
        @return: CreateIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ipam_pool_allocation_with_options(request, runtime)

    async def create_ipam_pool_allocation_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamPoolAllocationResponse:
        """
        @summary Reserves a custom CIDR block from an IP Address Manager (IPAM) pool.
        
        @description    Before you reserve a custom CIDR block, make sure that an IPAM pool is created and CIDR blocks are added to the pool. You can call **CreateIpamPool** to create an IPAM pool and call **AddIpamPoolCidr** to add CIDR blocks to the pool.
        When you specify Cidr or CidrMask to reserve a custom CIDR block, the mask must fall within the range specified by the IPAM pool.
        If the IPAM pool has the region attribute, you must reserve a custom CIDR block in the region to which the IPAM pool belongs.
        The custom CIDR block that you want to reserve cannot overlap with existing CIDR blocks created from the IPAM pool.
        
        @param request: CreateIpamPoolAllocationRequest
        @return: CreateIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ipam_pool_allocation_with_options_async(request, runtime)

    def create_ipam_resource_discovery_with_options(
        self,
        request: vpc_ipam_20230228_models.CreateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamResourceDiscoveryResponse:
        """
        @summary Creates a custom resource discovery instance.
        
        @description    Each Alibaba Cloud account can create only one resource discovery instance in each region.
        You can create only custom resource discovery instances.
        
        @param request: CreateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not UtilClient.is_unset(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not UtilClient.is_unset(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_resource_discovery_with_options_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamResourceDiscoveryResponse:
        """
        @summary Creates a custom resource discovery instance.
        
        @description    Each Alibaba Cloud account can create only one resource discovery instance in each region.
        You can create only custom resource discovery instances.
        
        @param request: CreateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not UtilClient.is_unset(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not UtilClient.is_unset(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_resource_discovery(
        self,
        request: vpc_ipam_20230228_models.CreateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamResourceDiscoveryResponse:
        """
        @summary Creates a custom resource discovery instance.
        
        @description    Each Alibaba Cloud account can create only one resource discovery instance in each region.
        You can create only custom resource discovery instances.
        
        @param request: CreateIpamResourceDiscoveryRequest
        @return: CreateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ipam_resource_discovery_with_options(request, runtime)

    async def create_ipam_resource_discovery_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamResourceDiscoveryResponse:
        """
        @summary Creates a custom resource discovery instance.
        
        @description    Each Alibaba Cloud account can create only one resource discovery instance in each region.
        You can create only custom resource discovery instances.
        
        @param request: CreateIpamResourceDiscoveryRequest
        @return: CreateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ipam_resource_discovery_with_options_async(request, runtime)

    def create_ipam_scope_with_options(
        self,
        request: vpc_ipam_20230228_models.CreateIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamScopeResponse:
        """
        @summary Creates a public scope and private scope to respectively manage public and private IP addresses.
        
        @param request: CreateIpamScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not UtilClient.is_unset(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not UtilClient.is_unset(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamScope',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_scope_with_options_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamScopeResponse:
        """
        @summary Creates a public scope and private scope to respectively manage public and private IP addresses.
        
        @param request: CreateIpamScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIpamScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not UtilClient.is_unset(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not UtilClient.is_unset(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIpamScope',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.CreateIpamScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_scope(
        self,
        request: vpc_ipam_20230228_models.CreateIpamScopeRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamScopeResponse:
        """
        @summary Creates a public scope and private scope to respectively manage public and private IP addresses.
        
        @param request: CreateIpamScopeRequest
        @return: CreateIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ipam_scope_with_options(request, runtime)

    async def create_ipam_scope_async(
        self,
        request: vpc_ipam_20230228_models.CreateIpamScopeRequest,
    ) -> vpc_ipam_20230228_models.CreateIpamScopeResponse:
        """
        @summary Creates a public scope and private scope to respectively manage public and private IP addresses.
        
        @param request: CreateIpamScopeRequest
        @return: CreateIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ipam_scope_with_options_async(request, runtime)

    def delete_ipam_with_options(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamResponse:
        """
        @summary Deletes an IP Address Manager (IPAM).
        
        @description ## [](#)Prerequisites
        Before you delete an IPAM, make sure that all IPAM pools of the IPAM are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        Before you delete an IPAM, make sure that all IPAM scopes of the IPAM are deleted. You can call **DeleteIpamScope** to delete IPAM scopes.
        
        @param request: DeleteIpamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
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
            action='DeleteIpam',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_with_options_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamResponse:
        """
        @summary Deletes an IP Address Manager (IPAM).
        
        @description ## [](#)Prerequisites
        Before you delete an IPAM, make sure that all IPAM pools of the IPAM are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        Before you delete an IPAM, make sure that all IPAM scopes of the IPAM are deleted. You can call **DeleteIpamScope** to delete IPAM scopes.
        
        @param request: DeleteIpamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
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
            action='DeleteIpam',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamResponse:
        """
        @summary Deletes an IP Address Manager (IPAM).
        
        @description ## [](#)Prerequisites
        Before you delete an IPAM, make sure that all IPAM pools of the IPAM are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        Before you delete an IPAM, make sure that all IPAM scopes of the IPAM are deleted. You can call **DeleteIpamScope** to delete IPAM scopes.
        
        @param request: DeleteIpamRequest
        @return: DeleteIpamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ipam_with_options(request, runtime)

    async def delete_ipam_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamResponse:
        """
        @summary Deletes an IP Address Manager (IPAM).
        
        @description ## [](#)Prerequisites
        Before you delete an IPAM, make sure that all IPAM pools of the IPAM are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        Before you delete an IPAM, make sure that all IPAM scopes of the IPAM are deleted. You can call **DeleteIpamScope** to delete IPAM scopes.
        
        @param request: DeleteIpamRequest
        @return: DeleteIpamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_with_options_async(request, runtime)

    def delete_ipam_pool_with_options(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        Before you delete a parent pool, make sure that all subpools of the parent pool are deleted.
        If an effective region is specified for a parent pool and IP addresses are allocated from the parent pool, you cannot delete the parent pool.
        If an effective region is specified for a subpool and IP addresses are allocated from the subpool, you cannot delete the subpool.
        
        @param request: DeleteIpamPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
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
            action='DeleteIpamPool',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_pool_with_options_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        Before you delete a parent pool, make sure that all subpools of the parent pool are deleted.
        If an effective region is specified for a parent pool and IP addresses are allocated from the parent pool, you cannot delete the parent pool.
        If an effective region is specified for a subpool and IP addresses are allocated from the subpool, you cannot delete the subpool.
        
        @param request: DeleteIpamPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
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
            action='DeleteIpamPool',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_pool(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        Before you delete a parent pool, make sure that all subpools of the parent pool are deleted.
        If an effective region is specified for a parent pool and IP addresses are allocated from the parent pool, you cannot delete the parent pool.
        If an effective region is specified for a subpool and IP addresses are allocated from the subpool, you cannot delete the subpool.
        
        @param request: DeleteIpamPoolRequest
        @return: DeleteIpamPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ipam_pool_with_options(request, runtime)

    async def delete_ipam_pool_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        Before you delete a parent pool, make sure that all subpools of the parent pool are deleted.
        If an effective region is specified for a parent pool and IP addresses are allocated from the parent pool, you cannot delete the parent pool.
        If an effective region is specified for a subpool and IP addresses are allocated from the subpool, you cannot delete the subpool.
        
        @param request: DeleteIpamPoolRequest
        @return: DeleteIpamPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_pool_with_options_async(request, runtime)

    def delete_ipam_pool_allocation_with_options(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolAllocationResponse:
        """
        @summary Deletes a custom reserved CIDR block from an IP Address Manager (IPAM) pool.
        
        @param request: DeleteIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_pool_allocation_with_options_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolAllocationResponse:
        """
        @summary Deletes a custom reserved CIDR block from an IP Address Manager (IPAM) pool.
        
        @param request: DeleteIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_pool_allocation(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolAllocationResponse:
        """
        @summary Deletes a custom reserved CIDR block from an IP Address Manager (IPAM) pool.
        
        @param request: DeleteIpamPoolAllocationRequest
        @return: DeleteIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ipam_pool_allocation_with_options(request, runtime)

    async def delete_ipam_pool_allocation_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolAllocationResponse:
        """
        @summary Deletes a custom reserved CIDR block from an IP Address Manager (IPAM) pool.
        
        @param request: DeleteIpamPoolAllocationRequest
        @return: DeleteIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_pool_allocation_with_options_async(request, runtime)

    def delete_ipam_pool_cidr_with_options(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolCidrResponse:
        """
        @summary Deletes a CIDR block provisioned to an IP Address Manager (IPAM) pool.
        
        @description    If CIDR blocks are provisioned to a parent pool and its subpools, you must first delete the CIDR blocks provisioned to the subpools before you delete the ones provisioned to the parent pool.
        If CIDR blocks are provisioned only to the parent pool, directly delete them.
        If CIDR blocks are allocated from provisioned ones, you must first delete the allocated CIDR blocks before you delete the provisioned ones.
        You can delete CIDR blocks provisioned to an IPAM pool only in the region where the IPAM is hosted.
        
        @param request: DeleteIpamPoolCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpamPoolCidr',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamPoolCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_pool_cidr_with_options_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolCidrResponse:
        """
        @summary Deletes a CIDR block provisioned to an IP Address Manager (IPAM) pool.
        
        @description    If CIDR blocks are provisioned to a parent pool and its subpools, you must first delete the CIDR blocks provisioned to the subpools before you delete the ones provisioned to the parent pool.
        If CIDR blocks are provisioned only to the parent pool, directly delete them.
        If CIDR blocks are allocated from provisioned ones, you must first delete the allocated CIDR blocks before you delete the provisioned ones.
        You can delete CIDR blocks provisioned to an IPAM pool only in the region where the IPAM is hosted.
        
        @param request: DeleteIpamPoolCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolCidrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIpamPoolCidr',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamPoolCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_pool_cidr(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolCidrRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolCidrResponse:
        """
        @summary Deletes a CIDR block provisioned to an IP Address Manager (IPAM) pool.
        
        @description    If CIDR blocks are provisioned to a parent pool and its subpools, you must first delete the CIDR blocks provisioned to the subpools before you delete the ones provisioned to the parent pool.
        If CIDR blocks are provisioned only to the parent pool, directly delete them.
        If CIDR blocks are allocated from provisioned ones, you must first delete the allocated CIDR blocks before you delete the provisioned ones.
        You can delete CIDR blocks provisioned to an IPAM pool only in the region where the IPAM is hosted.
        
        @param request: DeleteIpamPoolCidrRequest
        @return: DeleteIpamPoolCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ipam_pool_cidr_with_options(request, runtime)

    async def delete_ipam_pool_cidr_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamPoolCidrRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamPoolCidrResponse:
        """
        @summary Deletes a CIDR block provisioned to an IP Address Manager (IPAM) pool.
        
        @description    If CIDR blocks are provisioned to a parent pool and its subpools, you must first delete the CIDR blocks provisioned to the subpools before you delete the ones provisioned to the parent pool.
        If CIDR blocks are provisioned only to the parent pool, directly delete them.
        If CIDR blocks are allocated from provisioned ones, you must first delete the allocated CIDR blocks before you delete the provisioned ones.
        You can delete CIDR blocks provisioned to an IPAM pool only in the region where the IPAM is hosted.
        
        @param request: DeleteIpamPoolCidrRequest
        @return: DeleteIpamPoolCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_pool_cidr_with_options_async(request, runtime)

    def delete_ipam_resource_discovery_with_options(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryResponse:
        """
        @summary Deletes a custom resource discovery instance.
        
        @description    If a resource discovery instance is shared, it cannot be deleted.
        
        @param request: DeleteIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
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
            action='DeleteIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_resource_discovery_with_options_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryResponse:
        """
        @summary Deletes a custom resource discovery instance.
        
        @description    If a resource discovery instance is shared, it cannot be deleted.
        
        @param request: DeleteIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
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
            action='DeleteIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_resource_discovery(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryResponse:
        """
        @summary Deletes a custom resource discovery instance.
        
        @description    If a resource discovery instance is shared, it cannot be deleted.
        
        @param request: DeleteIpamResourceDiscoveryRequest
        @return: DeleteIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ipam_resource_discovery_with_options(request, runtime)

    async def delete_ipam_resource_discovery_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamResourceDiscoveryResponse:
        """
        @summary Deletes a custom resource discovery instance.
        
        @description    If a resource discovery instance is shared, it cannot be deleted.
        
        @param request: DeleteIpamResourceDiscoveryRequest
        @return: DeleteIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_resource_discovery_with_options_async(request, runtime)

    def delete_ipam_scope_with_options(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamScopeResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        You cannot delete the private scope and public scope created by the system.
        Before you delete an IPAM scope, make sure that all pools within the scope are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        
        @param request: DeleteIpamScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
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
            action='DeleteIpamScope',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_scope_with_options_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamScopeResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        You cannot delete the private scope and public scope created by the system.
        Before you delete an IPAM scope, make sure that all pools within the scope are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        
        @param request: DeleteIpamScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
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
            action='DeleteIpamScope',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DeleteIpamScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_scope(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamScopeRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamScopeResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        You cannot delete the private scope and public scope created by the system.
        Before you delete an IPAM scope, make sure that all pools within the scope are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        
        @param request: DeleteIpamScopeRequest
        @return: DeleteIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ipam_scope_with_options(request, runtime)

    async def delete_ipam_scope_async(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamScopeRequest,
    ) -> vpc_ipam_20230228_models.DeleteIpamScopeResponse:
        """
        @summary Deletes an IP Address Manager (IPAM) scope.
        
        @description ### [](#)Usage notes
        You cannot delete the private scope and public scope created by the system.
        Before you delete an IPAM scope, make sure that all pools within the scope are deleted. You can call **DeleteIpamPool** to delete IPAM pools.
        
        @param request: DeleteIpamScopeRequest
        @return: DeleteIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_scope_with_options_async(request, runtime)

    def dissociate_ipam_resource_discovery_with_options(
        self,
        request: vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryResponse:
        """
        @summary Disassociates resource discovery and IPAM instances.
        
        @param request: DissociateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
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
            action='DissociateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_ipam_resource_discovery_with_options_async(
        self,
        request: vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryResponse:
        """
        @summary Disassociates resource discovery and IPAM instances.
        
        @param request: DissociateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
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
            action='DissociateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_ipam_resource_discovery(
        self,
        request: vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryResponse:
        """
        @summary Disassociates resource discovery and IPAM instances.
        
        @param request: DissociateIpamResourceDiscoveryRequest
        @return: DissociateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dissociate_ipam_resource_discovery_with_options(request, runtime)

    async def dissociate_ipam_resource_discovery_async(
        self,
        request: vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.DissociateIpamResourceDiscoveryResponse:
        """
        @summary Disassociates resource discovery and IPAM instances.
        
        @param request: DissociateIpamResourceDiscoveryRequest
        @return: DissociateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_ipam_resource_discovery_with_options_async(request, runtime)

    def get_ipam_pool_allocation_with_options(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.GetIpamPoolAllocationResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: GetIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.GetIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ipam_pool_allocation_with_options_async(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.GetIpamPoolAllocationResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: GetIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.GetIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ipam_pool_allocation(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.GetIpamPoolAllocationResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: GetIpamPoolAllocationRequest
        @return: GetIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ipam_pool_allocation_with_options(request, runtime)

    async def get_ipam_pool_allocation_async(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.GetIpamPoolAllocationResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: GetIpamPoolAllocationRequest
        @return: GetIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ipam_pool_allocation_with_options_async(request, runtime)

    def get_ipam_pool_next_available_cidr_with_options(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrResponse:
        """
        @summary Gets the available CIDR blocks of the IPAM pool.
        
        @param request: GetIpamPoolNextAvailableCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpamPoolNextAvailableCidrResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIpamPoolNextAvailableCidr',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ipam_pool_next_available_cidr_with_options_async(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrResponse:
        """
        @summary Gets the available CIDR blocks of the IPAM pool.
        
        @param request: GetIpamPoolNextAvailableCidrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIpamPoolNextAvailableCidrResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIpamPoolNextAvailableCidr',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ipam_pool_next_available_cidr(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrRequest,
    ) -> vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrResponse:
        """
        @summary Gets the available CIDR blocks of the IPAM pool.
        
        @param request: GetIpamPoolNextAvailableCidrRequest
        @return: GetIpamPoolNextAvailableCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ipam_pool_next_available_cidr_with_options(request, runtime)

    async def get_ipam_pool_next_available_cidr_async(
        self,
        request: vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrRequest,
    ) -> vpc_ipam_20230228_models.GetIpamPoolNextAvailableCidrResponse:
        """
        @summary Gets the available CIDR blocks of the IPAM pool.
        
        @param request: GetIpamPoolNextAvailableCidrRequest
        @return: GetIpamPoolNextAvailableCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ipam_pool_next_available_cidr_with_options_async(request, runtime)

    def get_vpc_ipam_service_status_with_options(
        self,
        request: vpc_ipam_20230228_models.GetVpcIpamServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.GetVpcIpamServiceStatusResponse:
        """
        @summary Queries whether IP Address Manager (IPAM) is activated.
        
        @param request: GetVpcIpamServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpcIpamServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='GetVpcIpamServiceStatus',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.GetVpcIpamServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_ipam_service_status_with_options_async(
        self,
        request: vpc_ipam_20230228_models.GetVpcIpamServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.GetVpcIpamServiceStatusResponse:
        """
        @summary Queries whether IP Address Manager (IPAM) is activated.
        
        @param request: GetVpcIpamServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpcIpamServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='GetVpcIpamServiceStatus',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.GetVpcIpamServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_ipam_service_status(
        self,
        request: vpc_ipam_20230228_models.GetVpcIpamServiceStatusRequest,
    ) -> vpc_ipam_20230228_models.GetVpcIpamServiceStatusResponse:
        """
        @summary Queries whether IP Address Manager (IPAM) is activated.
        
        @param request: GetVpcIpamServiceStatusRequest
        @return: GetVpcIpamServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vpc_ipam_service_status_with_options(request, runtime)

    async def get_vpc_ipam_service_status_async(
        self,
        request: vpc_ipam_20230228_models.GetVpcIpamServiceStatusRequest,
    ) -> vpc_ipam_20230228_models.GetVpcIpamServiceStatusResponse:
        """
        @summary Queries whether IP Address Manager (IPAM) is activated.
        
        @param request: GetVpcIpamServiceStatusRequest
        @return: GetVpcIpamServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vpc_ipam_service_status_with_options_async(request, runtime)

    def list_ipam_discovered_resource_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamDiscoveredResourceResponse:
        """
        @summary Queries discovered resources.
        
        @param request: ListIpamDiscoveredResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamDiscoveredResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamDiscoveredResource',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_discovered_resource_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamDiscoveredResourceResponse:
        """
        @summary Queries discovered resources.
        
        @param request: ListIpamDiscoveredResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamDiscoveredResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamDiscoveredResource',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_discovered_resource(
        self,
        request: vpc_ipam_20230228_models.ListIpamDiscoveredResourceRequest,
    ) -> vpc_ipam_20230228_models.ListIpamDiscoveredResourceResponse:
        """
        @summary Queries discovered resources.
        
        @param request: ListIpamDiscoveredResourceRequest
        @return: ListIpamDiscoveredResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_discovered_resource_with_options(request, runtime)

    async def list_ipam_discovered_resource_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamDiscoveredResourceRequest,
    ) -> vpc_ipam_20230228_models.ListIpamDiscoveredResourceResponse:
        """
        @summary Queries discovered resources.
        
        @param request: ListIpamDiscoveredResourceRequest
        @return: ListIpamDiscoveredResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_discovered_resource_with_options_async(request, runtime)

    def list_ipam_pool_allocations_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolAllocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamPoolAllocationsResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolAllocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolAllocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.ipam_pool_allocation_ids):
            query['IpamPoolAllocationIds'] = request.ipam_pool_allocation_ids
        if not UtilClient.is_unset(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamPoolAllocations',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamPoolAllocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_pool_allocations_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolAllocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamPoolAllocationsResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolAllocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolAllocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.ipam_pool_allocation_ids):
            query['IpamPoolAllocationIds'] = request.ipam_pool_allocation_ids
        if not UtilClient.is_unset(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamPoolAllocations',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamPoolAllocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_pool_allocations(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolAllocationsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamPoolAllocationsResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolAllocationsRequest
        @return: ListIpamPoolAllocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_pool_allocations_with_options(request, runtime)

    async def list_ipam_pool_allocations_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolAllocationsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamPoolAllocationsResponse:
        """
        @summary Queries CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolAllocationsRequest
        @return: ListIpamPoolAllocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_pool_allocations_with_options_async(request, runtime)

    def list_ipam_pool_cidrs_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolCidrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamPoolCidrsResponse:
        """
        @summary Queries CIDR blocks provisioned to an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolCidrsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolCidrsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamPoolCidrs',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamPoolCidrsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_pool_cidrs_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolCidrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamPoolCidrsResponse:
        """
        @summary Queries CIDR blocks provisioned to an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolCidrsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolCidrsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamPoolCidrs',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamPoolCidrsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_pool_cidrs(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolCidrsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamPoolCidrsResponse:
        """
        @summary Queries CIDR blocks provisioned to an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolCidrsRequest
        @return: ListIpamPoolCidrsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_pool_cidrs_with_options(request, runtime)

    async def list_ipam_pool_cidrs_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolCidrsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamPoolCidrsResponse:
        """
        @summary Queries CIDR blocks provisioned to an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamPoolCidrsRequest
        @return: ListIpamPoolCidrsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_pool_cidrs_with_options_async(request, runtime)

    def list_ipam_pools_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamPoolsResponse:
        """
        @summary Queries IP Address Manager (IPAM) pools.
        
        @param request: ListIpamPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.ipam_pool_ids):
            query['IpamPoolIds'] = request.ipam_pool_ids
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not UtilClient.is_unset(request.is_shared):
            query['IsShared'] = request.is_shared
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamPools',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_pools_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamPoolsResponse:
        """
        @summary Queries IP Address Manager (IPAM) pools.
        
        @param request: ListIpamPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.ipam_pool_ids):
            query['IpamPoolIds'] = request.ipam_pool_ids
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not UtilClient.is_unset(request.is_shared):
            query['IsShared'] = request.is_shared
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamPools',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_pools(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamPoolsResponse:
        """
        @summary Queries IP Address Manager (IPAM) pools.
        
        @param request: ListIpamPoolsRequest
        @return: ListIpamPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_pools_with_options(request, runtime)

    async def list_ipam_pools_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamPoolsResponse:
        """
        @summary Queries IP Address Manager (IPAM) pools.
        
        @param request: ListIpamPoolsRequest
        @return: ListIpamPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_pools_with_options_async(request, runtime)

    def list_ipam_resource_cidrs_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceCidrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamResourceCidrsResponse:
        """
        @summary Queries resources in an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamResourceCidrsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamResourceCidrsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamResourceCidrs',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamResourceCidrsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_resource_cidrs_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceCidrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamResourceCidrsResponse:
        """
        @summary Queries resources in an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamResourceCidrsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamResourceCidrsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamResourceCidrs',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamResourceCidrsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_resource_cidrs(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceCidrsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamResourceCidrsResponse:
        """
        @summary Queries resources in an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamResourceCidrsRequest
        @return: ListIpamResourceCidrsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_resource_cidrs_with_options(request, runtime)

    async def list_ipam_resource_cidrs_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceCidrsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamResourceCidrsResponse:
        """
        @summary Queries resources in an IP Address Manager (IPAM) pool.
        
        @param request: ListIpamResourceCidrsRequest
        @return: ListIpamResourceCidrsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_resource_cidrs_with_options_async(request, runtime)

    def list_ipam_resource_discoveries_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveriesResponse:
        """
        @summary Queries IPAM resource discovery instances.
        
        @param request: ListIpamResourceDiscoveriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamResourceDiscoveriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_resource_discovery_ids):
            query['IpamResourceDiscoveryIds'] = request.ipam_resource_discovery_ids
        if not UtilClient.is_unset(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not UtilClient.is_unset(request.is_shared):
            query['IsShared'] = request.is_shared
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamResourceDiscoveries',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamResourceDiscoveriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_resource_discoveries_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveriesResponse:
        """
        @summary Queries IPAM resource discovery instances.
        
        @param request: ListIpamResourceDiscoveriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamResourceDiscoveriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_resource_discovery_ids):
            query['IpamResourceDiscoveryIds'] = request.ipam_resource_discovery_ids
        if not UtilClient.is_unset(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not UtilClient.is_unset(request.is_shared):
            query['IsShared'] = request.is_shared
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamResourceDiscoveries',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamResourceDiscoveriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_resource_discoveries(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveriesRequest,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveriesResponse:
        """
        @summary Queries IPAM resource discovery instances.
        
        @param request: ListIpamResourceDiscoveriesRequest
        @return: ListIpamResourceDiscoveriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_resource_discoveries_with_options(request, runtime)

    async def list_ipam_resource_discoveries_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveriesRequest,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveriesResponse:
        """
        @summary Queries IPAM resource discovery instances.
        
        @param request: ListIpamResourceDiscoveriesRequest
        @return: ListIpamResourceDiscoveriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_resource_discoveries_with_options_async(request, runtime)

    def list_ipam_resource_discovery_associations_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsResponse:
        """
        @summary Queries the association between resource discovery and IPAM.
        
        @param request: ListIpamResourceDiscoveryAssociationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamResourceDiscoveryAssociationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListIpamResourceDiscoveryAssociations',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_resource_discovery_associations_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsResponse:
        """
        @summary Queries the association between resource discovery and IPAM.
        
        @param request: ListIpamResourceDiscoveryAssociationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamResourceDiscoveryAssociationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListIpamResourceDiscoveryAssociations',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_resource_discovery_associations(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsResponse:
        """
        @summary Queries the association between resource discovery and IPAM.
        
        @param request: ListIpamResourceDiscoveryAssociationsRequest
        @return: ListIpamResourceDiscoveryAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_resource_discovery_associations_with_options(request, runtime)

    async def list_ipam_resource_discovery_associations_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamResourceDiscoveryAssociationsResponse:
        """
        @summary Queries the association between resource discovery and IPAM.
        
        @param request: ListIpamResourceDiscoveryAssociationsRequest
        @return: ListIpamResourceDiscoveryAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_resource_discovery_associations_with_options_async(request, runtime)

    def list_ipam_scopes_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamScopesResponse:
        """
        @summary Queries IP Address Manager (IPAM) scopes.
        
        @param request: ListIpamScopesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamScopesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_scope_ids):
            query['IpamScopeIds'] = request.ipam_scope_ids
        if not UtilClient.is_unset(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not UtilClient.is_unset(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamScopes',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamScopesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_scopes_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamScopesResponse:
        """
        @summary Queries IP Address Manager (IPAM) scopes.
        
        @param request: ListIpamScopesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamScopesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_scope_ids):
            query['IpamScopeIds'] = request.ipam_scope_ids
        if not UtilClient.is_unset(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not UtilClient.is_unset(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpamScopes',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamScopesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_scopes(
        self,
        request: vpc_ipam_20230228_models.ListIpamScopesRequest,
    ) -> vpc_ipam_20230228_models.ListIpamScopesResponse:
        """
        @summary Queries IP Address Manager (IPAM) scopes.
        
        @param request: ListIpamScopesRequest
        @return: ListIpamScopesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipam_scopes_with_options(request, runtime)

    async def list_ipam_scopes_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamScopesRequest,
    ) -> vpc_ipam_20230228_models.ListIpamScopesResponse:
        """
        @summary Queries IP Address Manager (IPAM) scopes.
        
        @param request: ListIpamScopesRequest
        @return: ListIpamScopesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_scopes_with_options_async(request, runtime)

    def list_ipams_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamsResponse:
        """
        @summary Queries IP Address Managers (IPAMs).
        
        @param request: ListIpamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_ids):
            query['IpamIds'] = request.ipam_ids
        if not UtilClient.is_unset(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpams',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipams_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamsResponse:
        """
        @summary Queries IP Address Managers (IPAMs).
        
        @param request: ListIpamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_ids):
            query['IpamIds'] = request.ipam_ids
        if not UtilClient.is_unset(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpams',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListIpamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipams(
        self,
        request: vpc_ipam_20230228_models.ListIpamsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamsResponse:
        """
        @summary Queries IP Address Managers (IPAMs).
        
        @param request: ListIpamsRequest
        @return: ListIpamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ipams_with_options(request, runtime)

    async def list_ipams_async(
        self,
        request: vpc_ipam_20230228_models.ListIpamsRequest,
    ) -> vpc_ipam_20230228_models.ListIpamsResponse:
        """
        @summary Queries IP Address Managers (IPAMs).
        
        @param request: ListIpamsRequest
        @return: ListIpamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipams_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: vpc_ipam_20230228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListTagResourcesResponse:
        """
        @summary Queries a list of resource tags.
        
        @description ### [](#)Usage notes
        You must specify **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object that you want to query.
        **Tag.N** is a resource tag that consists of a key-value pair. If you specify only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you specify only **Tag.N.Value**, an error message is returned.
        If you specify **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
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
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: vpc_ipam_20230228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListTagResourcesResponse:
        """
        @summary Queries a list of resource tags.
        
        @description ### [](#)Usage notes
        You must specify **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object that you want to query.
        **Tag.N** is a resource tag that consists of a key-value pair. If you specify only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you specify only **Tag.N.Value**, an error message is returned.
        If you specify **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
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
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: vpc_ipam_20230228_models.ListTagResourcesRequest,
    ) -> vpc_ipam_20230228_models.ListTagResourcesResponse:
        """
        @summary Queries a list of resource tags.
        
        @description ### [](#)Usage notes
        You must specify **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object that you want to query.
        **Tag.N** is a resource tag that consists of a key-value pair. If you specify only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you specify only **Tag.N.Value**, an error message is returned.
        If you specify **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: vpc_ipam_20230228_models.ListTagResourcesRequest,
    ) -> vpc_ipam_20230228_models.ListTagResourcesResponse:
        """
        @summary Queries a list of resource tags.
        
        @description ### [](#)Usage notes
        You must specify **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object that you want to query.
        **Tag.N** is a resource tag that consists of a key-value pair. If you specify only **Tag.N.Key**, all tag values that are associated with the specified key are returned. If you specify only **Tag.N.Value**, an error message is returned.
        If you specify **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def open_vpc_ipam_service_with_options(
        self,
        request: vpc_ipam_20230228_models.OpenVpcIpamServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.OpenVpcIpamServiceResponse:
        """
        @summary Activates IP Address Manager (IPAM).
        
        @param request: OpenVpcIpamServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenVpcIpamServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='OpenVpcIpamService',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.OpenVpcIpamServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_vpc_ipam_service_with_options_async(
        self,
        request: vpc_ipam_20230228_models.OpenVpcIpamServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.OpenVpcIpamServiceResponse:
        """
        @summary Activates IP Address Manager (IPAM).
        
        @param request: OpenVpcIpamServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenVpcIpamServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
            action='OpenVpcIpamService',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.OpenVpcIpamServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_vpc_ipam_service(
        self,
        request: vpc_ipam_20230228_models.OpenVpcIpamServiceRequest,
    ) -> vpc_ipam_20230228_models.OpenVpcIpamServiceResponse:
        """
        @summary Activates IP Address Manager (IPAM).
        
        @param request: OpenVpcIpamServiceRequest
        @return: OpenVpcIpamServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_vpc_ipam_service_with_options(request, runtime)

    async def open_vpc_ipam_service_async(
        self,
        request: vpc_ipam_20230228_models.OpenVpcIpamServiceRequest,
    ) -> vpc_ipam_20230228_models.OpenVpcIpamServiceResponse:
        """
        @summary Activates IP Address Manager (IPAM).
        
        @param request: OpenVpcIpamServiceRequest
        @return: OpenVpcIpamServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_vpc_ipam_service_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: vpc_ipam_20230228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.TagResourcesResponse:
        """
        @summary Adds a tag to a resource.
        
        @description ### [](#)Usage notes
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following items:
        Each tag key that is added to an instance must be unique.
        You cannot create tags without adding them to instances. All tags must be added to instances.
        You can add at most 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
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
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: vpc_ipam_20230228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.TagResourcesResponse:
        """
        @summary Adds a tag to a resource.
        
        @description ### [](#)Usage notes
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following items:
        Each tag key that is added to an instance must be unique.
        You cannot create tags without adding them to instances. All tags must be added to instances.
        You can add at most 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
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
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: vpc_ipam_20230228_models.TagResourcesRequest,
    ) -> vpc_ipam_20230228_models.TagResourcesResponse:
        """
        @summary Adds a tag to a resource.
        
        @description ### [](#)Usage notes
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following items:
        Each tag key that is added to an instance must be unique.
        You cannot create tags without adding them to instances. All tags must be added to instances.
        You can add at most 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: vpc_ipam_20230228_models.TagResourcesRequest,
    ) -> vpc_ipam_20230228_models.TagResourcesResponse:
        """
        @summary Adds a tag to a resource.
        
        @description ### [](#)Usage notes
        Tags are used to classify instances. Each tag consists of a key-value pair. Before you use tags, take note of the following items:
        Each tag key that is added to an instance must be unique.
        You cannot create tags without adding them to instances. All tags must be added to instances.
        You can add at most 20 tags to each instance. Before you add a tag to an instance, the system automatically checks the number of existing tags. An error message is returned if the maximum number of tags is reached.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: vpc_ipam_20230228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UntagResourcesResponse:
        """
        @summary Removes a tag from a resource.
        
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
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: vpc_ipam_20230228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UntagResourcesResponse:
        """
        @summary Removes a tag from a resource.
        
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
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: vpc_ipam_20230228_models.UntagResourcesRequest,
    ) -> vpc_ipam_20230228_models.UntagResourcesResponse:
        """
        @summary Removes a tag from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: vpc_ipam_20230228_models.UntagResourcesRequest,
    ) -> vpc_ipam_20230228_models.UntagResourcesResponse:
        """
        @summary Removes a tag from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_ipam_with_options(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamResponse:
        """
        @summary Updates an IP Address Manager (IPAM).
        
        @param request: UpdateIpamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpam',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_with_options_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamResponse:
        """
        @summary Updates an IP Address Manager (IPAM).
        
        @param request: UpdateIpamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not UtilClient.is_unset(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not UtilClient.is_unset(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpam',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamResponse:
        """
        @summary Updates an IP Address Manager (IPAM).
        
        @param request: UpdateIpamRequest
        @return: UpdateIpamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ipam_with_options(request, runtime)

    async def update_ipam_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamResponse:
        """
        @summary Updates an IP Address Manager (IPAM).
        
        @param request: UpdateIpamRequest
        @return: UpdateIpamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ipam_with_options_async(request, runtime)

    def update_ipam_pool_with_options(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not UtilClient.is_unset(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not UtilClient.is_unset(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not UtilClient.is_unset(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not UtilClient.is_unset(request.clear_allocation_default_cidr_mask):
            query['ClearAllocationDefaultCidrMask'] = request.clear_allocation_default_cidr_mask
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
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
            action='UpdateIpamPool',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_pool_with_options_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not UtilClient.is_unset(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not UtilClient.is_unset(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not UtilClient.is_unset(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not UtilClient.is_unset(request.clear_allocation_default_cidr_mask):
            query['ClearAllocationDefaultCidrMask'] = request.clear_allocation_default_cidr_mask
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
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
            action='UpdateIpamPool',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_pool(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolRequest
        @return: UpdateIpamPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ipam_pool_with_options(request, runtime)

    async def update_ipam_pool_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolRequest
        @return: UpdateIpamPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ipam_pool_with_options_async(request, runtime)

    def update_ipam_pool_allocation_with_options(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolAllocationResponse:
        """
        @summary Modifies CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not UtilClient.is_unset(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not UtilClient.is_unset(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_pool_allocation_with_options_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolAllocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolAllocationResponse:
        """
        @summary Modifies CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not UtilClient.is_unset(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not UtilClient.is_unset(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpamPoolAllocation',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_pool_allocation(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolAllocationResponse:
        """
        @summary Modifies CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolAllocationRequest
        @return: UpdateIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ipam_pool_allocation_with_options(request, runtime)

    async def update_ipam_pool_allocation_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamPoolAllocationRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamPoolAllocationResponse:
        """
        @summary Modifies CIDR block allocations of an IP Address Manager (IPAM) pool.
        
        @param request: UpdateIpamPoolAllocationRequest
        @return: UpdateIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ipam_pool_allocation_with_options_async(request, runtime)

    def update_ipam_resource_discovery_with_options(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryResponse:
        """
        @summary Modifies a resource discovery instance.
        
        @description    You can add or remove effective regions only for custom resource discovery instances.
        When removing effective regions from a resource discovery instance, the hosted region cannot be included.
        
        @param request: UpdateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_resource_discovery_with_options_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryResponse:
        """
        @summary Modifies a resource discovery instance.
        
        @description    You can add or remove effective regions only for custom resource discovery instances.
        When removing effective regions from a resource discovery instance, the hosted region cannot be included.
        
        @param request: UpdateIpamResourceDiscoveryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamResourceDiscoveryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not UtilClient.is_unset(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not UtilClient.is_unset(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIpamResourceDiscovery',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_resource_discovery(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryResponse:
        """
        @summary Modifies a resource discovery instance.
        
        @description    You can add or remove effective regions only for custom resource discovery instances.
        When removing effective regions from a resource discovery instance, the hosted region cannot be included.
        
        @param request: UpdateIpamResourceDiscoveryRequest
        @return: UpdateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ipam_resource_discovery_with_options(request, runtime)

    async def update_ipam_resource_discovery_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamResourceDiscoveryResponse:
        """
        @summary Modifies a resource discovery instance.
        
        @description    You can add or remove effective regions only for custom resource discovery instances.
        When removing effective regions from a resource discovery instance, the hosted region cannot be included.
        
        @param request: UpdateIpamResourceDiscoveryRequest
        @return: UpdateIpamResourceDiscoveryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ipam_resource_discovery_with_options_async(request, runtime)

    def update_ipam_scope_with_options(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamScopeResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) scope.
        
        @param request: UpdateIpamScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
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
            action='UpdateIpamScope',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_scope_with_options_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamScopeResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) scope.
        
        @param request: UpdateIpamScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIpamScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not UtilClient.is_unset(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
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
            action='UpdateIpamScope',
            version='2023-02-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vpc_ipam_20230228_models.UpdateIpamScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_scope(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamScopeRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamScopeResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) scope.
        
        @param request: UpdateIpamScopeRequest
        @return: UpdateIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ipam_scope_with_options(request, runtime)

    async def update_ipam_scope_async(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamScopeRequest,
    ) -> vpc_ipam_20230228_models.UpdateIpamScopeResponse:
        """
        @summary Modifies the basic information about an IP Address Manager (IPAM) scope.
        
        @param request: UpdateIpamScopeRequest
        @return: UpdateIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ipam_scope_with_options_async(request, runtime)
