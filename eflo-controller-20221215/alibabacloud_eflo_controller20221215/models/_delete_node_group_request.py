# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNodeGroupRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The node group ID.
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        return self

