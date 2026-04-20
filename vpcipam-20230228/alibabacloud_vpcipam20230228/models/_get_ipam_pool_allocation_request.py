# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIpamPoolAllocationRequest(DaraModel):
    def __init__(
        self,
        ipam_pool_allocation_id: str = None,
        region_id: str = None,
    ):
        # The ID of the instance to which CIDR blocks are allocated from the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The region of the IPAM pool.
        # 
        # >  If the IPAM pool to which CIDR allocation belongs has the region attribute, this parameter is the region of the IPAM pool. If not, this parameter is the IPAM hosted region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

