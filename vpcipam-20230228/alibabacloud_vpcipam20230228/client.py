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
        @param request: AddIpamPoolCidrRequest
        @return: AddIpamPoolCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_ipam_pool_cidr_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: vpc_ipam_20230228_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ChangeResourceGroupResponse:
        """
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
        @summary 创建IPAM实例。
        
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
        @summary 创建IPAM实例。
        
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
        @summary 创建IPAM实例。
        
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
        @summary 创建IPAM实例。
        
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
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
        @param request: CreateIpamPoolAllocationRequest
        @return: CreateIpamPoolAllocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ipam_pool_allocation_with_options_async(request, runtime)

    def create_ipam_scope_with_options(
        self,
        request: vpc_ipam_20230228_models.CreateIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.CreateIpamScopeResponse:
        """
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
        @param request: DeleteIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
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
        @param request: DeleteIpamPoolAllocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpamPoolAllocationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not UtilClient.is_unset(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
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
        @param request: DeleteIpamPoolCidrRequest
        @return: DeleteIpamPoolCidrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_pool_cidr_with_options_async(request, runtime)

    def delete_ipam_scope_with_options(
        self,
        request: vpc_ipam_20230228_models.DeleteIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.DeleteIpamScopeResponse:
        """
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
        @param request: DeleteIpamScopeRequest
        @return: DeleteIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipam_scope_with_options_async(request, runtime)

    def get_vpc_ipam_service_status_with_options(
        self,
        request: vpc_ipam_20230228_models.GetVpcIpamServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.GetVpcIpamServiceStatusResponse:
        """
        @summary 查询IPAM功能的开通状态。
        
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
        @summary 查询IPAM功能的开通状态。
        
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
        @summary 查询IPAM功能的开通状态。
        
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
        @summary 查询IPAM功能的开通状态。
        
        @param request: GetVpcIpamServiceStatusRequest
        @return: GetVpcIpamServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vpc_ipam_service_status_with_options_async(request, runtime)

    def list_ipam_pool_allocations_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamPoolAllocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamPoolAllocationsResponse:
        """
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
        @param request: ListIpamPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_pool_ids):
            query['IpamPoolIds'] = request.ipam_pool_ids
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
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
        @param request: ListIpamPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIpamPoolsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipam_pool_ids):
            query['IpamPoolIds'] = request.ipam_pool_ids
        if not UtilClient.is_unset(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not UtilClient.is_unset(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
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
        @param request: ListIpamResourceCidrsRequest
        @return: ListIpamResourceCidrsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ipam_resource_cidrs_with_options_async(request, runtime)

    def list_ipam_scopes_with_options(
        self,
        request: vpc_ipam_20230228_models.ListIpamScopesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.ListIpamScopesResponse:
        """
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
        @summary 查询ipam
        
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
        @summary 查询ipam
        
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
        @summary 查询ipam
        
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
        @summary 查询ipam
        
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
        @summary 查询资源标签列表
        
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
        @summary 查询资源标签列表
        
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
        @summary 查询资源标签列表
        
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
        @summary 查询资源标签列表
        
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
        @summary 开通IPAM功能。
        
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
        @summary 开通IPAM功能。
        
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
        @summary 开通IPAM功能。
        
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
        @summary 开通IPAM功能。
        
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
        @summary 为资源实例绑定资源标签
        
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
        @summary 为资源实例绑定资源标签
        
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
        @summary 为资源实例绑定资源标签
        
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
        @summary 为资源实例绑定资源标签
        
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
        @summary 为资源解绑资源标签
        
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
        @summary 为资源解绑资源标签
        
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
        @summary 为资源解绑资源标签
        
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
        @summary 为资源解绑资源标签
        
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
        @summary 更新ipam
        
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
        @summary 更新ipam
        
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
        @summary 更新ipam
        
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
        @summary 更新ipam
        
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
        @param request: UpdateIpamPoolRequest
        @return: UpdateIpamPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ipam_pool_with_options_async(request, runtime)

    def update_ipam_scope_with_options(
        self,
        request: vpc_ipam_20230228_models.UpdateIpamScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_ipam_20230228_models.UpdateIpamScopeResponse:
        """
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
        @param request: UpdateIpamScopeRequest
        @return: UpdateIpamScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ipam_scope_with_options_async(request, runtime)
