# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DecreaseNodesRequest(DaraModel):
    def __init__(
        self,
        batch_interval: int = None,
        batch_size: int = None,
        cluster_id: str = None,
        decrease_node_count: int = None,
        node_group_id: str = None,
        node_ids: List[str] = None,
        region_id: str = None,
    ):
        # The cooldown time between batches.
        self.batch_interval = batch_interval
        # The number of nodes to concurrently take offline in a single batch.
        self.batch_size = batch_size
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of nodes to remove. The value must be less than the number of active nodes in the node group.
        self.decrease_node_count = decrease_node_count
        # The node group ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # An array of node IDs. The array can contain from 1 to 500 elements.
        self.node_ids = node_ids
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
        if self.batch_interval is not None:
            result['BatchInterval'] = self.batch_interval

        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.decrease_node_count is not None:
            result['DecreaseNodeCount'] = self.decrease_node_count

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchInterval') is not None:
            self.batch_interval = m.get('BatchInterval')

        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DecreaseNodeCount') is not None:
            self.decrease_node_count = m.get('DecreaseNodeCount')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

