# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNodeGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group_shrink: str = None,
        node_unit_shrink: str = None,
    ):
        # Cluster ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Node ID.
        # 
        # This parameter is required.
        self.node_group_shrink = node_group_shrink
        # Node information
        self.node_unit_shrink = node_unit_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_group_shrink is not None:
            result['NodeGroup'] = self.node_group_shrink

        if self.node_unit_shrink is not None:
            result['NodeUnit'] = self.node_unit_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodeGroup') is not None:
            self.node_group_shrink = m.get('NodeGroup')

        if m.get('NodeUnit') is not None:
            self.node_unit_shrink = m.get('NodeUnit')

        return self

