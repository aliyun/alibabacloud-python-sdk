# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveNodePoolNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        concurrency: bool = None,
        drain_node: bool = None,
        instance_ids_shrink: str = None,
        nodes_shrink: str = None,
        release_node: bool = None,
    ):
        # Specifies whether to remove nodes concurrently.
        # 
        # - true: Nodes are concurrently removed from the scaling group.
        # 
        # - false: Nodes are sequentially removed from the scaling group.
        # 
        # Default value: false.
        self.concurrency = concurrency
        # Specifies whether to drain the nodes. Valid values:
        # - true: Drain the nodes.
        # - false: Do not drain the nodes.
        self.drain_node = drain_node
        # The list of instances to remove.
        self.instance_ids_shrink = instance_ids_shrink
        # [This parameter is deprecated]
        # 
        # The list of nodes to remove.
        # 
        # >Danger: This parameter is deprecated. Use `instance_ids` instead.</danger>.
        self.nodes_shrink = nodes_shrink
        # Specifies whether to release the nodes. Valid values:
        # - true: Release the nodes.
        # - false: Do not release the nodes.
        self.release_node = release_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency

        if self.drain_node is not None:
            result['drain_node'] = self.drain_node

        if self.instance_ids_shrink is not None:
            result['instance_ids'] = self.instance_ids_shrink

        if self.nodes_shrink is not None:
            result['nodes'] = self.nodes_shrink

        if self.release_node is not None:
            result['release_node'] = self.release_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')

        if m.get('instance_ids') is not None:
            self.instance_ids_shrink = m.get('instance_ids')

        if m.get('nodes') is not None:
            self.nodes_shrink = m.get('nodes')

        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')

        return self

