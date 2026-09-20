# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeNodeCountRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_count: int = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of core nodes in the cluster.
        # 
        # You can add up to 50 nodes at a time, and the total number of nodes can be scaled up to 250. If you have additional requirements, submit a ticket.
        # 
        # This parameter is required.
        self.node_count = node_count
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

