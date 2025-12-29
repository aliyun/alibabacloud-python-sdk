# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteClusterNodesRequest(DaraModel):
    def __init__(
        self,
        drain_node: bool = None,
        nodes: List[str] = None,
        release_node: bool = None,
    ):
        # Specifies whether to remove all pods from the nodes you want to remove. Valid values:
        # 
        # *   `true`: removes all pods automatically.
        # *   `false`: skips removing pods.
        # 
        # Default value: `false`
        self.drain_node = drain_node
        # The list of nodes to remove. You must specify the node names used in the cluster, for example, `cn-hangzhou.192.168.xx.xx`.
        # 
        # This parameter is required.
        self.nodes = nodes
        # Specifies whether to release the ECS instances. Valid values:
        # 
        # *   `true`: releases the ECS instances.
        # *   `false`: retains the ECS instances.
        # 
        # Default value: `false`
        # 
        # **
        # 
        # **Notes** Unsupported for subscription ECS instances.
        self.release_node = release_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node

        if self.nodes is not None:
            result['nodes'] = self.nodes

        if self.release_node is not None:
            result['release_node'] = self.release_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')

        return self

