# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssignNodeSpec(DaraModel):
    def __init__(
        self,
        anti_affinity_node_names: str = None,
        enable_assign_node: bool = None,
        node_names: str = None,
    ):
        self.anti_affinity_node_names = anti_affinity_node_names
        self.enable_assign_node = enable_assign_node
        self.node_names = node_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anti_affinity_node_names is not None:
            result['AntiAffinityNodeNames'] = self.anti_affinity_node_names

        if self.enable_assign_node is not None:
            result['EnableAssignNode'] = self.enable_assign_node

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiAffinityNodeNames') is not None:
            self.anti_affinity_node_names = m.get('AntiAffinityNodeNames')

        if m.get('EnableAssignNode') is not None:
            self.enable_assign_node = m.get('EnableAssignNode')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        return self

