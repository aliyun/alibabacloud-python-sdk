# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeDiskNodeGroupParam(DaraModel):
    def __init__(
        self,
        data_disk_capacity: int = None,
        node_group_id: str = None,
        rolling_restart: bool = None,
    ):
        self.data_disk_capacity = data_disk_capacity
        self.node_group_id = node_group_id
        self.rolling_restart = rolling_restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_capacity is not None:
            result['DataDiskCapacity'] = self.data_disk_capacity

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.rolling_restart is not None:
            result['RollingRestart'] = self.rolling_restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCapacity') is not None:
            self.data_disk_capacity = m.get('DataDiskCapacity')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('RollingRestart') is not None:
            self.rolling_restart = m.get('RollingRestart')

        return self

