# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClickhouseConf(DaraModel):
    def __init__(
        self,
        initial_replica: int = None,
        initial_shard: int = None,
        new_node_count: int = None,
        resize_type: str = None,
    ):
        self.initial_replica = initial_replica
        self.initial_shard = initial_shard
        self.new_node_count = new_node_count
        self.resize_type = resize_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.initial_replica is not None:
            result['InitialReplica'] = self.initial_replica

        if self.initial_shard is not None:
            result['InitialShard'] = self.initial_shard

        if self.new_node_count is not None:
            result['NewNodeCount'] = self.new_node_count

        if self.resize_type is not None:
            result['ResizeType'] = self.resize_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialReplica') is not None:
            self.initial_replica = m.get('InitialReplica')

        if m.get('InitialShard') is not None:
            self.initial_shard = m.get('InitialShard')

        if m.get('NewNodeCount') is not None:
            self.new_node_count = m.get('NewNodeCount')

        if m.get('ResizeType') is not None:
            self.resize_type = m.get('ResizeType')

        return self

