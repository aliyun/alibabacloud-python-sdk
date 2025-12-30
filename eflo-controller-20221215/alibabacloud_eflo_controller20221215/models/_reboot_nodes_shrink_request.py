# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
        self.nodes_shrink = nodes_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')

        return self

