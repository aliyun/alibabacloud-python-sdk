# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIpamPoolAllocationResponseBody(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        creation_time: str = None,
        ipam_pool_allocation_description: str = None,
        ipam_pool_allocation_id: str = None,
        ipam_pool_allocation_name: str = None,
        ipam_pool_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        resource_type: str = None,
        source_cidr: str = None,
        status: str = None,
    ):
        # The allocated CIDR block.
        self.cidr = cidr
        # The time when the instance was created.
        self.creation_time = creation_time
        # The description of the CIDR allocation of the IPAM pool.
        # 
        # The description must be 1 to 256 characters in length and start with a letter, but cannot start with a `http://` or `https://`. This parameter is empty by default.
        self.ipam_pool_allocation_description = ipam_pool_allocation_description
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The name of the CIDR allocation of the IPAM pool.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The region of the IPAM pool.
        # 
        # >  If the IPAM pool to which the CIDR block allocation belongs has the region attribute, this parameter is the region of the IPAM pool. If not, this parameter is the IPAM hosted region.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource to which the CIDR block is allocated.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_owner_id = resource_owner_id
        # The effective region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of the resource to which the CIDR block is allocated. Valid values:
        # 
        # *   **VPC**
        # *   **IpamPool**
        # *   **Custom**
        self.resource_type = resource_type
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The instance state. Valid values:
        # 
        # *   **Created**
        # *   **Deleted**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ipam_pool_allocation_description is not None:
            result['IpamPoolAllocationDescription'] = self.ipam_pool_allocation_description

        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id

        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IpamPoolAllocationDescription') is not None:
            self.ipam_pool_allocation_description = m.get('IpamPoolAllocationDescription')

        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')

        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

