# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeMultiZoneClusterNodeCountRequest(DaraModel):
    def __init__(
        self,
        arbiter_vswitch_id: str = None,
        cluster_id: str = None,
        core_node_count: int = None,
        log_node_count: int = None,
        primary_core_node_count: int = None,
        primary_vswitch_id: str = None,
        standby_core_node_count: int = None,
        standby_vswitch_id: str = None,
    ):
        # The vSwitch ID of the arbitration node.
        self.arbiter_vswitch_id = arbiter_vswitch_id
        # The ID of the multi-zone cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of core nodes. The minimum value is 4, and the increment must be a multiple of 2.
        self.core_node_count = core_node_count
        # The number of log nodes. The minimum value is 4, and the value must be a multiple of 4.
        self.log_node_count = log_node_count
        # The number of core nodes in the primary zone instance. The minimum value is 4, and the increment must be a multiple of 2.
        self.primary_core_node_count = primary_core_node_count
        # The vSwitch ID of the instance in the primary zone.
        self.primary_vswitch_id = primary_vswitch_id
        # The number of core nodes in the secondary zone instance. The minimum value is 4, and the increment must be a multiple of 2.
        self.standby_core_node_count = standby_core_node_count
        # The vSwitch ID of the instance in the secondary zone.
        self.standby_vswitch_id = standby_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count

        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count

        if self.primary_core_node_count is not None:
            result['PrimaryCoreNodeCount'] = self.primary_core_node_count

        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id

        if self.standby_core_node_count is not None:
            result['StandbyCoreNodeCount'] = self.standby_core_node_count

        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')

        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')

        if m.get('PrimaryCoreNodeCount') is not None:
            self.primary_core_node_count = m.get('PrimaryCoreNodeCount')

        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')

        if m.get('StandbyCoreNodeCount') is not None:
            self.standby_core_node_count = m.get('StandbyCoreNodeCount')

        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')

        return self

