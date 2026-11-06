# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveNodePoolNodesRequest(DaraModel):
    def __init__(
        self,
        concurrency: bool = None,
        drain_node: bool = None,
        drain_timeout_seconds: int = None,
        instance_ids: List[str] = None,
        nodes: List[str] = None,
        release_node: bool = None,
    ):
        # Specifies whether to remove nodes concurrently. Valid values:
        # - true: Nodes are removed from the scaling group concurrently.
        # - false: Nodes are removed from the scaling group sequentially.
        # 
        # Default value: false.
        self.concurrency = concurrency
        # Specifies whether to drain the nodes. Valid values:
        # - true: Drain the nodes.
        # - false: Do not drain the nodes.
        self.drain_node = drain_node
        # The drain timeout period in seconds. Valid values: (0, 1800]. Default value: 1800. This parameter takes effect only when drain_node is set to true.
        self.drain_timeout_seconds = drain_timeout_seconds
        # The list of instances to be removed.
        self.instance_ids = instance_ids
        # **[Deprecated]**
        # 
        # The list of nodes to be removed.
        # 
        # >Danger: This parameter is deprecated. Use `instance_ids` instead.</danger>
        self.nodes = nodes
        # Specifies whether automatic release the nodes. Valid values:
        # - true: Release the nodes.
        # - false: Do not release the nodes.
        # 
        # Removing nodes does not automatically release subscription nodes. Automatic release subscription nodes, [change the billing method of the nodes from subscription to pay-as-you-go](https://www.alibabacloud.com/help/en/ecs/change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1), and then log on to the ECS console automatic release them.
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

        if self.drain_timeout_seconds is not None:
            result['drain_timeout_seconds'] = self.drain_timeout_seconds

        if self.instance_ids is not None:
            result['instance_ids'] = self.instance_ids

        if self.nodes is not None:
            result['nodes'] = self.nodes

        if self.release_node is not None:
            result['release_node'] = self.release_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')

        if m.get('drain_timeout_seconds') is not None:
            self.drain_timeout_seconds = m.get('drain_timeout_seconds')

        if m.get('instance_ids') is not None:
            self.instance_ids = m.get('instance_ids')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')

        return self

