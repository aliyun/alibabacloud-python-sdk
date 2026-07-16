# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListIpamPoolAllocationsRequest(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        ipam_pool_allocation_ids: List[str] = None,
        ipam_pool_allocation_name: str = None,
        ipam_pool_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The allocated CIDR block that you want to query.
        # 
        # > Only IPv4 CIDR blocks are supported.
        self.cidr = cidr
        # A list of instance IDs of the IPAM pool CIDR block allocations.
        self.ipam_pool_allocation_ids = ipam_pool_allocation_ids
        # The name of the IPAM pool CIDR block allocation.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_pool_allocation_name = ipam_pool_allocation_name
        # The instance ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The maximum number of entries to return on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # - If **NextToken** is empty, no next page exists.
        # 
        # - If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The region of the IPAM pool that contains the CIDR block allocation.
        # 
        # > If the IPAM pool has a specific region, this parameter specifies that region. If the IPAM pool does not have a specific region, this parameter specifies the managed region of IPAM.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.ipam_pool_allocation_ids is not None:
            result['IpamPoolAllocationIds'] = self.ipam_pool_allocation_ids

        if self.ipam_pool_allocation_name is not None:
            result['IpamPoolAllocationName'] = self.ipam_pool_allocation_name

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('IpamPoolAllocationIds') is not None:
            self.ipam_pool_allocation_ids = m.get('IpamPoolAllocationIds')

        if m.get('IpamPoolAllocationName') is not None:
            self.ipam_pool_allocation_name = m.get('IpamPoolAllocationName')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

