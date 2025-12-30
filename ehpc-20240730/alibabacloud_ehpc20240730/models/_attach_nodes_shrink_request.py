# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        compute_node_shrink: str = None,
        queue_name: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The list of compute nodes.
        # 
        # This parameter is required.
        self.compute_node_shrink = compute_node_shrink
        # The name of the queue to which the instance is to be added.
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.compute_node_shrink is not None:
            result['ComputeNode'] = self.compute_node_shrink

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComputeNode') is not None:
            self.compute_node_shrink = m.get('ComputeNode')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        return self

