# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ChangeNodeGroupRequest(DaraModel):
    def __init__(
        self,
        ignore_failed_node_tasks: bool = None,
        nodes: List[str] = None,
        target_node_group_id: str = None,
    ):
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.nodes = nodes
        self.target_node_group_id = target_node_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        if self.nodes is not None:
            result['Nodes'] = self.nodes

        if self.target_node_group_id is not None:
            result['TargetNodeGroupId'] = self.target_node_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')

        if m.get('TargetNodeGroupId') is not None:
            self.target_node_group_id = m.get('TargetNodeGroupId')

        return self

