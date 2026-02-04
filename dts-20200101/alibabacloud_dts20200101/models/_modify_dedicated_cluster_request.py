# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDedicatedClusterRequest(DaraModel):
    def __init__(
        self,
        dedicated_cluster_id: str = None,
        dedicated_cluster_name: str = None,
        instance_id: str = None,
        oversold_ratio: int = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # >  You must specify one of the **InstanceId** and **DedicatedClusterId** parameters.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The name of the cluster.
        self.dedicated_cluster_name = dedicated_cluster_name
        # The ID of the instance.
        # 
        # >  You must specify one of the **InstanceId** and **DedicatedClusterId** parameters.
        self.instance_id = instance_id
        # The overcommit ratio. Unit: %.
        self.oversold_ratio = oversold_ratio
        self.owner_id = owner_id
        # The ID of the region in which the Data Transmission Service (DTS) instance resides.
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

        if self.dedicated_cluster_name is not None:
            result['DedicatedClusterName'] = self.dedicated_cluster_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.oversold_ratio is not None:
            result['OversoldRatio'] = self.oversold_ratio

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

        if m.get('DedicatedClusterName') is not None:
            self.dedicated_cluster_name = m.get('DedicatedClusterName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OversoldRatio') is not None:
            self.oversold_ratio = m.get('OversoldRatio')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

