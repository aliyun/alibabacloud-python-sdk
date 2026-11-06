# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteClusterNodesRequest(DaraModel):
    def __init__(
        self,
        drain_node: bool = None,
        drain_timeout_seconds: int = None,
        nodes: List[str] = None,
        release_node: bool = None,
    ):
        # Specifies whether to automatically drain pods from the nodes. Valid values:
        # - `true`: Automatically drains pods from the nodes.
        # - `false`: Does not automatically drain pods from the nodes.
        # 
        # Default value: `false`.
        self.drain_node = drain_node
        # The drain timeout period in seconds. Valid values: (0, 1800]. If this parameter is not specified, the default value 1800 is used. This parameter takes effect only when drain_node is set to true.
        self.drain_timeout_seconds = drain_timeout_seconds
        # The list of nodes to remove. The node name must be the name of the node in the cluster, such as `cn-hangzhou.192.168.xx.xx`.
        # 
        # This parameter is required.
        self.nodes = nodes
        # Specifies whether to release the associated ECS instances. Valid values:
        # 
        # - `true`: Releases the associated ECS instances.
        # - `false`: Retains the associated ECS instances.
        # 
        # Default value: `false`.
        # 
        # > When a node is a subscription instance, you cannot release the associated ECS instance.
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

        if self.drain_timeout_seconds is not None:
            result['drain_timeout_seconds'] = self.drain_timeout_seconds

        if self.nodes is not None:
            result['nodes'] = self.nodes

        if self.release_node is not None:
            result['release_node'] = self.release_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')

        if m.get('drain_timeout_seconds') is not None:
            self.drain_timeout_seconds = m.get('drain_timeout_seconds')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')

        return self

