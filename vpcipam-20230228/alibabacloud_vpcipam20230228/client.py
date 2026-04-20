# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_ipam_members_with_options(
        self,
        request: main_models.AddIpamMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpamMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpamMembers',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpamMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ipam_members_with_options_async(
        self,
        request: main_models.AddIpamMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpamMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpamMembers',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpamMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ipam_members(
        self,
        request: main_models.AddIpamMembersRequest,
    ) -> main_models.AddIpamMembersResponse:
        runtime = RuntimeOptions()
        return self.add_ipam_members_with_options(request, runtime)

    async def add_ipam_members_async(
        self,
        request: main_models.AddIpamMembersRequest,
    ) -> main_models.AddIpamMembersResponse:
        runtime = RuntimeOptions()
        return await self.add_ipam_members_with_options_async(request, runtime)

    def add_ipam_pool_cidr_with_options(
        self,
        request: main_models.AddIpamPoolCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpamPoolCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.netmask_length):
            query['NetmaskLength'] = request.netmask_length
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpamPoolCidr',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpamPoolCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ipam_pool_cidr_with_options_async(
        self,
        request: main_models.AddIpamPoolCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIpamPoolCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.netmask_length):
            query['NetmaskLength'] = request.netmask_length
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIpamPoolCidr',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIpamPoolCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ipam_pool_cidr(
        self,
        request: main_models.AddIpamPoolCidrRequest,
    ) -> main_models.AddIpamPoolCidrResponse:
        runtime = RuntimeOptions()
        return self.add_ipam_pool_cidr_with_options(request, runtime)

    async def add_ipam_pool_cidr_async(
        self,
        request: main_models.AddIpamPoolCidrRequest,
    ) -> main_models.AddIpamPoolCidrResponse:
        runtime = RuntimeOptions()
        return await self.add_ipam_pool_cidr_with_options_async(request, runtime)

    def associate_ipam_resource_discovery_with_options(
        self,
        request: main_models.AssociateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_ipam_resource_discovery_with_options_async(
        self,
        request: main_models.AssociateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_ipam_resource_discovery(
        self,
        request: main_models.AssociateIpamResourceDiscoveryRequest,
    ) -> main_models.AssociateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return self.associate_ipam_resource_discovery_with_options(request, runtime)

    async def associate_ipam_resource_discovery_async(
        self,
        request: main_models.AssociateIpamResourceDiscoveryRequest,
    ) -> main_models.AssociateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return await self.associate_ipam_resource_discovery_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_ipam_with_options(
        self,
        request: main_models.CreateIpamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not DaraCore.is_null(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not DaraCore.is_null(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpam',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_with_options_async(
        self,
        request: main_models.CreateIpamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not DaraCore.is_null(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not DaraCore.is_null(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpam',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam(
        self,
        request: main_models.CreateIpamRequest,
    ) -> main_models.CreateIpamResponse:
        runtime = RuntimeOptions()
        return self.create_ipam_with_options(request, runtime)

    async def create_ipam_async(
        self,
        request: main_models.CreateIpamRequest,
    ) -> main_models.CreateIpamResponse:
        runtime = RuntimeOptions()
        return await self.create_ipam_with_options_async(request, runtime)

    def create_ipam_pool_with_options(
        self,
        request: main_models.CreateIpamPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not DaraCore.is_null(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not DaraCore.is_null(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not DaraCore.is_null(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not DaraCore.is_null(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamPool',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_pool_with_options_async(
        self,
        request: main_models.CreateIpamPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not DaraCore.is_null(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not DaraCore.is_null(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not DaraCore.is_null(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not DaraCore.is_null(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamPool',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_pool(
        self,
        request: main_models.CreateIpamPoolRequest,
    ) -> main_models.CreateIpamPoolResponse:
        runtime = RuntimeOptions()
        return self.create_ipam_pool_with_options(request, runtime)

    async def create_ipam_pool_async(
        self,
        request: main_models.CreateIpamPoolRequest,
    ) -> main_models.CreateIpamPoolResponse:
        runtime = RuntimeOptions()
        return await self.create_ipam_pool_with_options_async(request, runtime)

    def create_ipam_pool_allocation_with_options(
        self,
        request: main_models.CreateIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamPoolAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.cidr_mask):
            query['CidrMask'] = request.cidr_mask
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not DaraCore.is_null(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_pool_allocation_with_options_async(
        self,
        request: main_models.CreateIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamPoolAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.cidr_mask):
            query['CidrMask'] = request.cidr_mask
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not DaraCore.is_null(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_pool_allocation(
        self,
        request: main_models.CreateIpamPoolAllocationRequest,
    ) -> main_models.CreateIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return self.create_ipam_pool_allocation_with_options(request, runtime)

    async def create_ipam_pool_allocation_async(
        self,
        request: main_models.CreateIpamPoolAllocationRequest,
    ) -> main_models.CreateIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return await self.create_ipam_pool_allocation_with_options_async(request, runtime)

    def create_ipam_resource_discovery_with_options(
        self,
        request: main_models.CreateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not DaraCore.is_null(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not DaraCore.is_null(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_resource_discovery_with_options_async(
        self,
        request: main_models.CreateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not DaraCore.is_null(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not DaraCore.is_null(request.operating_region_list):
            query['OperatingRegionList'] = request.operating_region_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_resource_discovery(
        self,
        request: main_models.CreateIpamResourceDiscoveryRequest,
    ) -> main_models.CreateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return self.create_ipam_resource_discovery_with_options(request, runtime)

    async def create_ipam_resource_discovery_async(
        self,
        request: main_models.CreateIpamResourceDiscoveryRequest,
    ) -> main_models.CreateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return await self.create_ipam_resource_discovery_with_options_async(request, runtime)

    def create_ipam_scope_with_options(
        self,
        request: main_models.CreateIpamScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not DaraCore.is_null(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not DaraCore.is_null(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamScope',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ipam_scope_with_options_async(
        self,
        request: main_models.CreateIpamScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpamScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not DaraCore.is_null(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not DaraCore.is_null(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpamScope',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpamScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ipam_scope(
        self,
        request: main_models.CreateIpamScopeRequest,
    ) -> main_models.CreateIpamScopeResponse:
        runtime = RuntimeOptions()
        return self.create_ipam_scope_with_options(request, runtime)

    async def create_ipam_scope_async(
        self,
        request: main_models.CreateIpamScopeRequest,
    ) -> main_models.CreateIpamScopeResponse:
        runtime = RuntimeOptions()
        return await self.create_ipam_scope_with_options_async(request, runtime)

    def delete_ipam_with_options(
        self,
        request: main_models.DeleteIpamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpam',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_with_options_async(
        self,
        request: main_models.DeleteIpamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpam',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam(
        self,
        request: main_models.DeleteIpamRequest,
    ) -> main_models.DeleteIpamResponse:
        runtime = RuntimeOptions()
        return self.delete_ipam_with_options(request, runtime)

    async def delete_ipam_async(
        self,
        request: main_models.DeleteIpamRequest,
    ) -> main_models.DeleteIpamResponse:
        runtime = RuntimeOptions()
        return await self.delete_ipam_with_options_async(request, runtime)

    def delete_ipam_pool_with_options(
        self,
        request: main_models.DeleteIpamPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamPool',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_pool_with_options_async(
        self,
        request: main_models.DeleteIpamPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamPool',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_pool(
        self,
        request: main_models.DeleteIpamPoolRequest,
    ) -> main_models.DeleteIpamPoolResponse:
        runtime = RuntimeOptions()
        return self.delete_ipam_pool_with_options(request, runtime)

    async def delete_ipam_pool_async(
        self,
        request: main_models.DeleteIpamPoolRequest,
    ) -> main_models.DeleteIpamPoolResponse:
        runtime = RuntimeOptions()
        return await self.delete_ipam_pool_with_options_async(request, runtime)

    def delete_ipam_pool_allocation_with_options(
        self,
        request: main_models.DeleteIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamPoolAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_pool_allocation_with_options_async(
        self,
        request: main_models.DeleteIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamPoolAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_pool_allocation(
        self,
        request: main_models.DeleteIpamPoolAllocationRequest,
    ) -> main_models.DeleteIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return self.delete_ipam_pool_allocation_with_options(request, runtime)

    async def delete_ipam_pool_allocation_async(
        self,
        request: main_models.DeleteIpamPoolAllocationRequest,
    ) -> main_models.DeleteIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return await self.delete_ipam_pool_allocation_with_options_async(request, runtime)

    def delete_ipam_pool_cidr_with_options(
        self,
        request: main_models.DeleteIpamPoolCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamPoolCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamPoolCidr',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamPoolCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_pool_cidr_with_options_async(
        self,
        request: main_models.DeleteIpamPoolCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamPoolCidrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamPoolCidr',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamPoolCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_pool_cidr(
        self,
        request: main_models.DeleteIpamPoolCidrRequest,
    ) -> main_models.DeleteIpamPoolCidrResponse:
        runtime = RuntimeOptions()
        return self.delete_ipam_pool_cidr_with_options(request, runtime)

    async def delete_ipam_pool_cidr_async(
        self,
        request: main_models.DeleteIpamPoolCidrRequest,
    ) -> main_models.DeleteIpamPoolCidrResponse:
        runtime = RuntimeOptions()
        return await self.delete_ipam_pool_cidr_with_options_async(request, runtime)

    def delete_ipam_resource_discovery_with_options(
        self,
        request: main_models.DeleteIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_resource_discovery_with_options_async(
        self,
        request: main_models.DeleteIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_resource_discovery(
        self,
        request: main_models.DeleteIpamResourceDiscoveryRequest,
    ) -> main_models.DeleteIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return self.delete_ipam_resource_discovery_with_options(request, runtime)

    async def delete_ipam_resource_discovery_async(
        self,
        request: main_models.DeleteIpamResourceDiscoveryRequest,
    ) -> main_models.DeleteIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return await self.delete_ipam_resource_discovery_with_options_async(request, runtime)

    def delete_ipam_scope_with_options(
        self,
        request: main_models.DeleteIpamScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamScope',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ipam_scope_with_options_async(
        self,
        request: main_models.DeleteIpamScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpamScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpamScope',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpamScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ipam_scope(
        self,
        request: main_models.DeleteIpamScopeRequest,
    ) -> main_models.DeleteIpamScopeResponse:
        runtime = RuntimeOptions()
        return self.delete_ipam_scope_with_options(request, runtime)

    async def delete_ipam_scope_async(
        self,
        request: main_models.DeleteIpamScopeRequest,
    ) -> main_models.DeleteIpamScopeResponse:
        runtime = RuntimeOptions()
        return await self.delete_ipam_scope_with_options_async(request, runtime)

    def dissociate_ipam_resource_discovery_with_options(
        self,
        request: main_models.DissociateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_ipam_resource_discovery_with_options_async(
        self,
        request: main_models.DissociateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DissociateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_ipam_resource_discovery(
        self,
        request: main_models.DissociateIpamResourceDiscoveryRequest,
    ) -> main_models.DissociateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return self.dissociate_ipam_resource_discovery_with_options(request, runtime)

    async def dissociate_ipam_resource_discovery_async(
        self,
        request: main_models.DissociateIpamResourceDiscoveryRequest,
    ) -> main_models.DissociateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return await self.dissociate_ipam_resource_discovery_with_options_async(request, runtime)

    def get_ipam_pool_allocation_with_options(
        self,
        request: main_models.GetIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpamPoolAllocationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ipam_pool_allocation_with_options_async(
        self,
        request: main_models.GetIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpamPoolAllocationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ipam_pool_allocation(
        self,
        request: main_models.GetIpamPoolAllocationRequest,
    ) -> main_models.GetIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return self.get_ipam_pool_allocation_with_options(request, runtime)

    async def get_ipam_pool_allocation_async(
        self,
        request: main_models.GetIpamPoolAllocationRequest,
    ) -> main_models.GetIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return await self.get_ipam_pool_allocation_with_options_async(request, runtime)

    def get_ipam_pool_next_available_cidr_with_options(
        self,
        request: main_models.GetIpamPoolNextAvailableCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpamPoolNextAvailableCidrResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpamPoolNextAvailableCidr',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpamPoolNextAvailableCidrResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ipam_pool_next_available_cidr_with_options_async(
        self,
        request: main_models.GetIpamPoolNextAvailableCidrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpamPoolNextAvailableCidrResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpamPoolNextAvailableCidr',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpamPoolNextAvailableCidrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ipam_pool_next_available_cidr(
        self,
        request: main_models.GetIpamPoolNextAvailableCidrRequest,
    ) -> main_models.GetIpamPoolNextAvailableCidrResponse:
        runtime = RuntimeOptions()
        return self.get_ipam_pool_next_available_cidr_with_options(request, runtime)

    async def get_ipam_pool_next_available_cidr_async(
        self,
        request: main_models.GetIpamPoolNextAvailableCidrRequest,
    ) -> main_models.GetIpamPoolNextAvailableCidrResponse:
        runtime = RuntimeOptions()
        return await self.get_ipam_pool_next_available_cidr_with_options_async(request, runtime)

    def get_vpc_ipam_service_status_with_options(
        self,
        request: main_models.GetVpcIpamServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcIpamServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcIpamServiceStatus',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcIpamServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpc_ipam_service_status_with_options_async(
        self,
        request: main_models.GetVpcIpamServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVpcIpamServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVpcIpamServiceStatus',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVpcIpamServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpc_ipam_service_status(
        self,
        request: main_models.GetVpcIpamServiceStatusRequest,
    ) -> main_models.GetVpcIpamServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_vpc_ipam_service_status_with_options(request, runtime)

    async def get_vpc_ipam_service_status_async(
        self,
        request: main_models.GetVpcIpamServiceStatusRequest,
    ) -> main_models.GetVpcIpamServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_vpc_ipam_service_status_with_options_async(request, runtime)

    def list_ipam_discovered_ip_addresses_with_options(
        self,
        request: main_models.ListIpamDiscoveredIpAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamDiscoveredIpAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamDiscoveredIpAddresses',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamDiscoveredIpAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_discovered_ip_addresses_with_options_async(
        self,
        request: main_models.ListIpamDiscoveredIpAddressesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamDiscoveredIpAddressesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamDiscoveredIpAddresses',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamDiscoveredIpAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_discovered_ip_addresses(
        self,
        request: main_models.ListIpamDiscoveredIpAddressesRequest,
    ) -> main_models.ListIpamDiscoveredIpAddressesResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_discovered_ip_addresses_with_options(request, runtime)

    async def list_ipam_discovered_ip_addresses_async(
        self,
        request: main_models.ListIpamDiscoveredIpAddressesRequest,
    ) -> main_models.ListIpamDiscoveredIpAddressesResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_discovered_ip_addresses_with_options_async(request, runtime)

    def list_ipam_discovered_resource_with_options(
        self,
        request: main_models.ListIpamDiscoveredResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamDiscoveredResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamDiscoveredResource',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_discovered_resource_with_options_async(
        self,
        request: main_models.ListIpamDiscoveredResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamDiscoveredResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamDiscoveredResource',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_discovered_resource(
        self,
        request: main_models.ListIpamDiscoveredResourceRequest,
    ) -> main_models.ListIpamDiscoveredResourceResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_discovered_resource_with_options(request, runtime)

    async def list_ipam_discovered_resource_async(
        self,
        request: main_models.ListIpamDiscoveredResourceRequest,
    ) -> main_models.ListIpamDiscoveredResourceResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_discovered_resource_with_options_async(request, runtime)

    def list_ipam_members_with_options(
        self,
        request: main_models.ListIpamMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.member_ids):
            query['MemberIds'] = request.member_ids
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamMembers',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_members_with_options_async(
        self,
        request: main_models.ListIpamMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.member_ids):
            query['MemberIds'] = request.member_ids
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamMembers',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_members(
        self,
        request: main_models.ListIpamMembersRequest,
    ) -> main_models.ListIpamMembersResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_members_with_options(request, runtime)

    async def list_ipam_members_async(
        self,
        request: main_models.ListIpamMembersRequest,
    ) -> main_models.ListIpamMembersResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_members_with_options_async(request, runtime)

    def list_ipam_pool_allocations_with_options(
        self,
        request: main_models.ListIpamPoolAllocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamPoolAllocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.ipam_pool_allocation_ids):
            query['IpamPoolAllocationIds'] = request.ipam_pool_allocation_ids
        if not DaraCore.is_null(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamPoolAllocations',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamPoolAllocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_pool_allocations_with_options_async(
        self,
        request: main_models.ListIpamPoolAllocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamPoolAllocationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.ipam_pool_allocation_ids):
            query['IpamPoolAllocationIds'] = request.ipam_pool_allocation_ids
        if not DaraCore.is_null(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamPoolAllocations',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamPoolAllocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_pool_allocations(
        self,
        request: main_models.ListIpamPoolAllocationsRequest,
    ) -> main_models.ListIpamPoolAllocationsResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_pool_allocations_with_options(request, runtime)

    async def list_ipam_pool_allocations_async(
        self,
        request: main_models.ListIpamPoolAllocationsRequest,
    ) -> main_models.ListIpamPoolAllocationsResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_pool_allocations_with_options_async(request, runtime)

    def list_ipam_pool_cidrs_with_options(
        self,
        request: main_models.ListIpamPoolCidrsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamPoolCidrsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamPoolCidrs',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamPoolCidrsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_pool_cidrs_with_options_async(
        self,
        request: main_models.ListIpamPoolCidrsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamPoolCidrsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamPoolCidrs',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamPoolCidrsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_pool_cidrs(
        self,
        request: main_models.ListIpamPoolCidrsRequest,
    ) -> main_models.ListIpamPoolCidrsResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_pool_cidrs_with_options(request, runtime)

    async def list_ipam_pool_cidrs_async(
        self,
        request: main_models.ListIpamPoolCidrsRequest,
    ) -> main_models.ListIpamPoolCidrsResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_pool_cidrs_with_options_async(request, runtime)

    def list_ipam_pools_with_options(
        self,
        request: main_models.ListIpamPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.ipam_pool_ids):
            query['IpamPoolIds'] = request.ipam_pool_ids
        if not DaraCore.is_null(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not DaraCore.is_null(request.is_shared):
            query['IsShared'] = request.is_shared
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamPools',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_pools_with_options_async(
        self,
        request: main_models.ListIpamPoolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamPoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.ipam_pool_ids):
            query['IpamPoolIds'] = request.ipam_pool_ids
        if not DaraCore.is_null(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.ipv_6isp):
            query['Ipv6Isp'] = request.ipv_6isp
        if not DaraCore.is_null(request.is_shared):
            query['IsShared'] = request.is_shared
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pool_region_id):
            query['PoolRegionId'] = request.pool_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_ipam_pool_id):
            query['SourceIpamPoolId'] = request.source_ipam_pool_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamPools',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_pools(
        self,
        request: main_models.ListIpamPoolsRequest,
    ) -> main_models.ListIpamPoolsResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_pools_with_options(request, runtime)

    async def list_ipam_pools_async(
        self,
        request: main_models.ListIpamPoolsRequest,
    ) -> main_models.ListIpamPoolsResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_pools_with_options_async(request, runtime)

    def list_ipam_resource_cidrs_with_options(
        self,
        request: main_models.ListIpamResourceCidrsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamResourceCidrsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamResourceCidrs',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamResourceCidrsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_resource_cidrs_with_options_async(
        self,
        request: main_models.ListIpamResourceCidrsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamResourceCidrsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamResourceCidrs',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamResourceCidrsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_resource_cidrs(
        self,
        request: main_models.ListIpamResourceCidrsRequest,
    ) -> main_models.ListIpamResourceCidrsResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_resource_cidrs_with_options(request, runtime)

    async def list_ipam_resource_cidrs_async(
        self,
        request: main_models.ListIpamResourceCidrsRequest,
    ) -> main_models.ListIpamResourceCidrsResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_resource_cidrs_with_options_async(request, runtime)

    def list_ipam_resource_discoveries_with_options(
        self,
        request: main_models.ListIpamResourceDiscoveriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamResourceDiscoveriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_resource_discovery_ids):
            query['IpamResourceDiscoveryIds'] = request.ipam_resource_discovery_ids
        if not DaraCore.is_null(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not DaraCore.is_null(request.is_shared):
            query['IsShared'] = request.is_shared
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamResourceDiscoveries',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamResourceDiscoveriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_resource_discoveries_with_options_async(
        self,
        request: main_models.ListIpamResourceDiscoveriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamResourceDiscoveriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_resource_discovery_ids):
            query['IpamResourceDiscoveryIds'] = request.ipam_resource_discovery_ids
        if not DaraCore.is_null(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not DaraCore.is_null(request.is_shared):
            query['IsShared'] = request.is_shared
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamResourceDiscoveries',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamResourceDiscoveriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_resource_discoveries(
        self,
        request: main_models.ListIpamResourceDiscoveriesRequest,
    ) -> main_models.ListIpamResourceDiscoveriesResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_resource_discoveries_with_options(request, runtime)

    async def list_ipam_resource_discoveries_async(
        self,
        request: main_models.ListIpamResourceDiscoveriesRequest,
    ) -> main_models.ListIpamResourceDiscoveriesResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_resource_discoveries_with_options_async(request, runtime)

    def list_ipam_resource_discovery_associations_with_options(
        self,
        request: main_models.ListIpamResourceDiscoveryAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamResourceDiscoveryAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamResourceDiscoveryAssociations',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamResourceDiscoveryAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_resource_discovery_associations_with_options_async(
        self,
        request: main_models.ListIpamResourceDiscoveryAssociationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamResourceDiscoveryAssociationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamResourceDiscoveryAssociations',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamResourceDiscoveryAssociationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_resource_discovery_associations(
        self,
        request: main_models.ListIpamResourceDiscoveryAssociationsRequest,
    ) -> main_models.ListIpamResourceDiscoveryAssociationsResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_resource_discovery_associations_with_options(request, runtime)

    async def list_ipam_resource_discovery_associations_async(
        self,
        request: main_models.ListIpamResourceDiscoveryAssociationsRequest,
    ) -> main_models.ListIpamResourceDiscoveryAssociationsResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_resource_discovery_associations_with_options_async(request, runtime)

    def list_ipam_scopes_with_options(
        self,
        request: main_models.ListIpamScopesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamScopesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_scope_ids):
            query['IpamScopeIds'] = request.ipam_scope_ids
        if not DaraCore.is_null(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not DaraCore.is_null(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamScopes',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamScopesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipam_scopes_with_options_async(
        self,
        request: main_models.ListIpamScopesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamScopesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_scope_ids):
            query['IpamScopeIds'] = request.ipam_scope_ids
        if not DaraCore.is_null(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not DaraCore.is_null(request.ipam_scope_type):
            query['IpamScopeType'] = request.ipam_scope_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpamScopes',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamScopesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipam_scopes(
        self,
        request: main_models.ListIpamScopesRequest,
    ) -> main_models.ListIpamScopesResponse:
        runtime = RuntimeOptions()
        return self.list_ipam_scopes_with_options(request, runtime)

    async def list_ipam_scopes_async(
        self,
        request: main_models.ListIpamScopesRequest,
    ) -> main_models.ListIpamScopesResponse:
        runtime = RuntimeOptions()
        return await self.list_ipam_scopes_with_options_async(request, runtime)

    def list_ipams_with_options(
        self,
        request: main_models.ListIpamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_ids):
            query['IpamIds'] = request.ipam_ids
        if not DaraCore.is_null(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpams',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ipams_with_options_async(
        self,
        request: main_models.ListIpamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipam_ids):
            query['IpamIds'] = request.ipam_ids
        if not DaraCore.is_null(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpams',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ipams(
        self,
        request: main_models.ListIpamsRequest,
    ) -> main_models.ListIpamsResponse:
        runtime = RuntimeOptions()
        return self.list_ipams_with_options(request, runtime)

    async def list_ipams_async(
        self,
        request: main_models.ListIpamsRequest,
    ) -> main_models.ListIpamsResponse:
        runtime = RuntimeOptions()
        return await self.list_ipams_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def open_vpc_ipam_service_with_options(
        self,
        request: main_models.OpenVpcIpamServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenVpcIpamServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenVpcIpamService',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenVpcIpamServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_vpc_ipam_service_with_options_async(
        self,
        request: main_models.OpenVpcIpamServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenVpcIpamServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenVpcIpamService',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenVpcIpamServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_vpc_ipam_service(
        self,
        request: main_models.OpenVpcIpamServiceRequest,
    ) -> main_models.OpenVpcIpamServiceResponse:
        runtime = RuntimeOptions()
        return self.open_vpc_ipam_service_with_options(request, runtime)

    async def open_vpc_ipam_service_async(
        self,
        request: main_models.OpenVpcIpamServiceRequest,
    ) -> main_models.OpenVpcIpamServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_vpc_ipam_service_with_options_async(request, runtime)

    def remove_ipam_members_with_options(
        self,
        request: main_models.RemoveIpamMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpamMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpamMembers',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpamMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ipam_members_with_options_async(
        self,
        request: main_models.RemoveIpamMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveIpamMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveIpamMembers',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveIpamMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ipam_members(
        self,
        request: main_models.RemoveIpamMembersRequest,
    ) -> main_models.RemoveIpamMembersResponse:
        runtime = RuntimeOptions()
        return self.remove_ipam_members_with_options(request, runtime)

    async def remove_ipam_members_async(
        self,
        request: main_models.RemoveIpamMembersRequest,
    ) -> main_models.RemoveIpamMembersResponse:
        runtime = RuntimeOptions()
        return await self.remove_ipam_members_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_ipam_with_options(
        self,
        request: main_models.UpdateIpamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpam',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_with_options_async(
        self,
        request: main_models.UpdateIpamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_description):
            query['IpamDescription'] = request.ipam_description
        if not DaraCore.is_null(request.ipam_id):
            query['IpamId'] = request.ipam_id
        if not DaraCore.is_null(request.ipam_name):
            query['IpamName'] = request.ipam_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpam',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam(
        self,
        request: main_models.UpdateIpamRequest,
    ) -> main_models.UpdateIpamResponse:
        runtime = RuntimeOptions()
        return self.update_ipam_with_options(request, runtime)

    async def update_ipam_async(
        self,
        request: main_models.UpdateIpamRequest,
    ) -> main_models.UpdateIpamResponse:
        runtime = RuntimeOptions()
        return await self.update_ipam_with_options_async(request, runtime)

    def update_ipam_pool_with_options(
        self,
        request: main_models.UpdateIpamPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not DaraCore.is_null(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not DaraCore.is_null(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not DaraCore.is_null(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not DaraCore.is_null(request.clear_allocation_default_cidr_mask):
            query['ClearAllocationDefaultCidrMask'] = request.clear_allocation_default_cidr_mask
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamPool',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_pool_with_options_async(
        self,
        request: main_models.UpdateIpamPoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamPoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allocation_default_cidr_mask):
            query['AllocationDefaultCidrMask'] = request.allocation_default_cidr_mask
        if not DaraCore.is_null(request.allocation_max_cidr_mask):
            query['AllocationMaxCidrMask'] = request.allocation_max_cidr_mask
        if not DaraCore.is_null(request.allocation_min_cidr_mask):
            query['AllocationMinCidrMask'] = request.allocation_min_cidr_mask
        if not DaraCore.is_null(request.auto_import):
            query['AutoImport'] = request.auto_import
        if not DaraCore.is_null(request.clear_allocation_default_cidr_mask):
            query['ClearAllocationDefaultCidrMask'] = request.clear_allocation_default_cidr_mask
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_description):
            query['IpamPoolDescription'] = request.ipam_pool_description
        if not DaraCore.is_null(request.ipam_pool_id):
            query['IpamPoolId'] = request.ipam_pool_id
        if not DaraCore.is_null(request.ipam_pool_name):
            query['IpamPoolName'] = request.ipam_pool_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamPool',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_pool(
        self,
        request: main_models.UpdateIpamPoolRequest,
    ) -> main_models.UpdateIpamPoolResponse:
        runtime = RuntimeOptions()
        return self.update_ipam_pool_with_options(request, runtime)

    async def update_ipam_pool_async(
        self,
        request: main_models.UpdateIpamPoolRequest,
    ) -> main_models.UpdateIpamPoolResponse:
        runtime = RuntimeOptions()
        return await self.update_ipam_pool_with_options_async(request, runtime)

    def update_ipam_pool_allocation_with_options(
        self,
        request: main_models.UpdateIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamPoolAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not DaraCore.is_null(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not DaraCore.is_null(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamPoolAllocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_pool_allocation_with_options_async(
        self,
        request: main_models.UpdateIpamPoolAllocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamPoolAllocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_pool_allocation_description):
            query['IpamPoolAllocationDescription'] = request.ipam_pool_allocation_description
        if not DaraCore.is_null(request.ipam_pool_allocation_id):
            query['IpamPoolAllocationId'] = request.ipam_pool_allocation_id
        if not DaraCore.is_null(request.ipam_pool_allocation_name):
            query['IpamPoolAllocationName'] = request.ipam_pool_allocation_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamPoolAllocation',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamPoolAllocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_pool_allocation(
        self,
        request: main_models.UpdateIpamPoolAllocationRequest,
    ) -> main_models.UpdateIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return self.update_ipam_pool_allocation_with_options(request, runtime)

    async def update_ipam_pool_allocation_async(
        self,
        request: main_models.UpdateIpamPoolAllocationRequest,
    ) -> main_models.UpdateIpamPoolAllocationResponse:
        runtime = RuntimeOptions()
        return await self.update_ipam_pool_allocation_with_options_async(request, runtime)

    def update_ipam_resource_discovery_with_options(
        self,
        request: main_models.UpdateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamResourceDiscoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_resource_discovery_with_options_async(
        self,
        request: main_models.UpdateIpamResourceDiscoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamResourceDiscoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_operating_region):
            query['AddOperatingRegion'] = request.add_operating_region
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_resource_discovery_description):
            query['IpamResourceDiscoveryDescription'] = request.ipam_resource_discovery_description
        if not DaraCore.is_null(request.ipam_resource_discovery_id):
            query['IpamResourceDiscoveryId'] = request.ipam_resource_discovery_id
        if not DaraCore.is_null(request.ipam_resource_discovery_name):
            query['IpamResourceDiscoveryName'] = request.ipam_resource_discovery_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_operating_region):
            query['RemoveOperatingRegion'] = request.remove_operating_region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamResourceDiscovery',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamResourceDiscoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_resource_discovery(
        self,
        request: main_models.UpdateIpamResourceDiscoveryRequest,
    ) -> main_models.UpdateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return self.update_ipam_resource_discovery_with_options(request, runtime)

    async def update_ipam_resource_discovery_async(
        self,
        request: main_models.UpdateIpamResourceDiscoveryRequest,
    ) -> main_models.UpdateIpamResourceDiscoveryResponse:
        runtime = RuntimeOptions()
        return await self.update_ipam_resource_discovery_with_options_async(request, runtime)

    def update_ipam_scope_with_options(
        self,
        request: main_models.UpdateIpamScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamScope',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ipam_scope_with_options_async(
        self,
        request: main_models.UpdateIpamScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpamScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.ipam_scope_description):
            query['IpamScopeDescription'] = request.ipam_scope_description
        if not DaraCore.is_null(request.ipam_scope_id):
            query['IpamScopeId'] = request.ipam_scope_id
        if not DaraCore.is_null(request.ipam_scope_name):
            query['IpamScopeName'] = request.ipam_scope_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpamScope',
            version = '2023-02-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpamScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ipam_scope(
        self,
        request: main_models.UpdateIpamScopeRequest,
    ) -> main_models.UpdateIpamScopeResponse:
        runtime = RuntimeOptions()
        return self.update_ipam_scope_with_options(request, runtime)

    async def update_ipam_scope_async(
        self,
        request: main_models.UpdateIpamScopeRequest,
    ) -> main_models.UpdateIpamScopeResponse:
        runtime = RuntimeOptions()
        return await self.update_ipam_scope_with_options_async(request, runtime)
