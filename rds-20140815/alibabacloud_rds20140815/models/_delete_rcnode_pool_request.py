# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRCNodePoolRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_pool_id: str = None,
        region_id: str = None,
    ):
        # The ID of the ACK cluster to which the RDS Custom instance belongs.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The node pool ID.
        # 
        # This parameter is required.
        self.node_pool_id = node_pool_id
        # The region ID.
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

