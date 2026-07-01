# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIpamDiscoveredResourceRequest(DaraModel):
    def __init__(
        self,
        ipam_resource_discovery_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The resource discovery instance ID.
        # 
        # This parameter is required.
        self.ipam_resource_discovery_id = ipam_resource_discovery_id
        # The maximum number of entries to return per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token. Valid values:
        # 
        # - If this is the first query or no subsequent query exists, leave this parameter empty.
        # - If a subsequent query exists, set this parameter to the **NextToken** value returned in the previous API call.
        self.next_token = next_token
        # The hosted region ID of the resource discovery instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The operating region of the resource discovery.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The resource type. Valid values:
        # 
        # - **VPC**: VPC.
        # 
        # - **VSwitch**: vSwitch.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipam_resource_discovery_id is not None:
            result['IpamResourceDiscoveryId'] = self.ipam_resource_discovery_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamResourceDiscoveryId') is not None:
            self.ipam_resource_discovery_id = m.get('IpamResourceDiscoveryId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

