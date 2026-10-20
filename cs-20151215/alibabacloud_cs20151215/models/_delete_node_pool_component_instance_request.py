# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteNodePoolComponentInstanceRequest(DaraModel):
    def __init__(
        self,
        batch_interval: int = None,
        max_failed_nodes: int = None,
        max_parallelism: int = None,
        node_names: List[str] = None,
        pause_policy: str = None,
    ):
        # The interval between batches, in seconds. Default value: 0.
        self.batch_interval = batch_interval
        # The maximum number of nodes that can fail during the rolling process. Default value: 0. A value of 0 indicates that the task fails if any node fails. A value greater than 0 indicates that the task fails and stops if the cumulative number of failed nodes exceeds this value.
        self.max_failed_nodes = max_failed_nodes
        # The maximum number of parallel operations per batch. Default value: 1.
        self.max_parallelism = max_parallelism
        # The list of nodes to rotate. Default value: all nodes.
        self.node_names = node_names
        # The auto-pause policy during a node upgrade. Valid values:
        # - NotPause
        # - FirstBatch
        # - EveryBatch
        # 
        # Default value: NotPause.
        self.pause_policy = pause_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_interval is not None:
            result['batch_interval'] = self.batch_interval

        if self.max_failed_nodes is not None:
            result['max_failed_nodes'] = self.max_failed_nodes

        if self.max_parallelism is not None:
            result['max_parallelism'] = self.max_parallelism

        if self.node_names is not None:
            result['node_names'] = self.node_names

        if self.pause_policy is not None:
            result['pause_policy'] = self.pause_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batch_interval') is not None:
            self.batch_interval = m.get('batch_interval')

        if m.get('max_failed_nodes') is not None:
            self.max_failed_nodes = m.get('max_failed_nodes')

        if m.get('max_parallelism') is not None:
            self.max_parallelism = m.get('max_parallelism')

        if m.get('node_names') is not None:
            self.node_names = m.get('node_names')

        if m.get('pause_policy') is not None:
            self.pause_policy = m.get('pause_policy')

        return self

