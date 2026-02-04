# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDedicatedClusterRequest(DaraModel):
    def __init__(
        self,
        dedicated_cluster_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dedicated_cluster_id = dedicated_cluster_id
        self.owner_id = owner_id
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

