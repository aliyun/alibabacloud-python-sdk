# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateHoneypotNodeRequest(DaraModel):
    def __init__(
        self,
        available_probe_num: int = None,
        node_id: str = None,
        node_name: str = None,
        security_group_probe_ip_list: List[str] = None,
    ):
        # The number of available probes.
        # 
        # This parameter is required.
        self.available_probe_num = available_probe_num
        # The ID of the management node.
        # 
        # > You can call the [ListHoneypotNode](~~ListHoneypotNode~~) operation to query the IDs of management nodes.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The name of the management node.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The CIDR blocks that are allowed to access the management node.
        self.security_group_probe_ip_list = security_group_probe_ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_probe_num is not None:
            result['AvailableProbeNum'] = self.available_probe_num

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.security_group_probe_ip_list is not None:
            result['SecurityGroupProbeIpList'] = self.security_group_probe_ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableProbeNum') is not None:
            self.available_probe_num = m.get('AvailableProbeNum')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('SecurityGroupProbeIpList') is not None:
            self.security_group_probe_ip_list = m.get('SecurityGroupProbeIpList')

        return self

