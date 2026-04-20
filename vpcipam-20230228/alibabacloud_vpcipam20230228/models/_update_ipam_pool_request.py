# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIpamPoolRequest(DaraModel):
    def __init__(
        self,
        allocation_default_cidr_mask: int = None,
        allocation_max_cidr_mask: int = None,
        allocation_min_cidr_mask: int = None,
        auto_import: bool = None,
        clear_allocation_default_cidr_mask: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_description: str = None,
        ipam_pool_id: str = None,
        ipam_pool_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The new default network mask for the IPAM pool.
        # 
        # The mask must be **0 to 32** bits in length.
        self.allocation_default_cidr_mask = allocation_default_cidr_mask
        # The new maximum network mask for the IPAM pool.
        # 
        # The mask must be **0 to 32** bits in length.
        self.allocation_max_cidr_mask = allocation_max_cidr_mask
        # The new minimum network mask for the IPAM pool.
        # 
        # The mask must be **0 to 32** bits in length.
        self.allocation_min_cidr_mask = allocation_min_cidr_mask
        # Whether the pool has the auto-import feature enabled.
        self.auto_import = auto_import
        # Specifies whether to delete the default network mask for the IPAM pool. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.clear_allocation_default_cidr_mask = clear_allocation_default_cidr_mask
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The new description of the IPAM pool.
        # 
        # It must be 2 to 268 characters in length. It must start with a letter but cannot start with a `http://` or `https://`. This parameter is empty by default.
        self.ipam_pool_description = ipam_pool_description
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The new name of the IPAM pool.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_name = ipam_pool_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_default_cidr_mask is not None:
            result['AllocationDefaultCidrMask'] = self.allocation_default_cidr_mask

        if self.allocation_max_cidr_mask is not None:
            result['AllocationMaxCidrMask'] = self.allocation_max_cidr_mask

        if self.allocation_min_cidr_mask is not None:
            result['AllocationMinCidrMask'] = self.allocation_min_cidr_mask

        if self.auto_import is not None:
            result['AutoImport'] = self.auto_import

        if self.clear_allocation_default_cidr_mask is not None:
            result['ClearAllocationDefaultCidrMask'] = self.clear_allocation_default_cidr_mask

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipam_pool_description is not None:
            result['IpamPoolDescription'] = self.ipam_pool_description

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.ipam_pool_name is not None:
            result['IpamPoolName'] = self.ipam_pool_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationDefaultCidrMask') is not None:
            self.allocation_default_cidr_mask = m.get('AllocationDefaultCidrMask')

        if m.get('AllocationMaxCidrMask') is not None:
            self.allocation_max_cidr_mask = m.get('AllocationMaxCidrMask')

        if m.get('AllocationMinCidrMask') is not None:
            self.allocation_min_cidr_mask = m.get('AllocationMinCidrMask')

        if m.get('AutoImport') is not None:
            self.auto_import = m.get('AutoImport')

        if m.get('ClearAllocationDefaultCidrMask') is not None:
            self.clear_allocation_default_cidr_mask = m.get('ClearAllocationDefaultCidrMask')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpamPoolDescription') is not None:
            self.ipam_pool_description = m.get('IpamPoolDescription')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('IpamPoolName') is not None:
            self.ipam_pool_name = m.get('IpamPoolName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

