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
        # Whether to remove concurrently.
        self.concurrency = concurrency
        # Specifies whether to drain the nodes that you want to remove. Valid values:
        # 
        # *   true: drain the nodes that you want to remove.
        # *   false: do not drain the nodes that you want to remove.
        self.drain_node = drain_node
        # A list of instances that you want to remove.
        self.instance_ids_shrink = instance_ids_shrink
        # This parameter is deprecated.
        # 
        # A list of nodes that you want to remove.
        # 
        # >  This parameter is deprecated. Use instance_ids instead.
        self.nodes_shrink = nodes_shrink
        # Specifies whether to release the nodes after they are removed. Valid values:
        # 
        # *   true: release the nodes after they are removed.
        # *   false: do not release the nodes after they are removed.
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

