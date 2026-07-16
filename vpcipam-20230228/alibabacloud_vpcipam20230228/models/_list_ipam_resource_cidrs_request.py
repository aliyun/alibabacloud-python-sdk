# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIpamResourceCidrsRequest(DaraModel):
    def __init__(
        self,
        ipam_pool_id: str = None,
        ipam_scope_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        vpc_id: str = None,
    ):
        # The instance ID of the IPAM pool.
        # 
        # > **IpamPoolId** cannot be the instance ID of a shared IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The instance ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The maximum number of entries to return per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token. Valid values:
        # 
        # - If this is the first request or no more results exist, leave this parameter empty.
        # - If more results exist, set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The ID of the region where IPAM is hosted.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID.
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # - **VPC**: The resource type is VPC.
        # - **VSwitch**: The resource type is vSwitch.
        self.resource_type = resource_type
        # The instance ID of the VPC-connected instance to which the resource belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

