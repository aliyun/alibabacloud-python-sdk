# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RefreshNodeGroupNodesRequest(DaraModel):
    def __init__(
        self,
        max_disruptive_action: str = None,
        node_group_id: str = None,
        node_ids: List[str] = None,
    ):
        # The maximum disruptive action level allowed for the refresh operation. The system independently evaluates the action level required to refresh each drifted property of a node and performs the refresh within the specified action level constraint. If the action level required for a property exceeds the specified level, that property is skipped. Action levels in increasing order of disruption: Refresh < Reboot < Reimage.
        # - Refresh (default): refreshes the configuration in place without restarting or reimaging. Currently applicable only to the RamRoleName property.
        # - Reboot (not currently supported): allows restarting the node for the configuration to take effect. Supported properties include system cloud disk type and all properties supported by Refresh.
        # - Reimage (not currently supported): allows reimaging the node for the configuration to take effect. Supported properties include image ID and all properties supported by Reboot.
        self.max_disruptive_action = max_disruptive_action
        # The node group ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The filter scope for node refresh. If not specified, all nodes in the node group are included. <warning>If the instance type is a hypernode, pass the TrayNode ID, not the HyperNodeId.</warning>
        self.node_ids = node_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_disruptive_action is not None:
            result['MaxDisruptiveAction'] = self.max_disruptive_action

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxDisruptiveAction') is not None:
            self.max_disruptive_action = m.get('MaxDisruptiveAction')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        return self

