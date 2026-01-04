# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceNetworkAttributeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        private_ip_address: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the ENS instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new private IP address of the ECS instance. By default, if this parameter is empty, a private IP address is randomly assigned from the CIDR block of the specified vSwitch.
        self.private_ip_address = private_ip_address
        # The vSwitch IDs.
        # 
        # *   If you set this parameter to the ID of the current vSwitch, the vSwitch of the ECS instance remains unchanged.
        # *   The input ID is a new vSwitch, and the new and old vSwitches must belong to the same node.
        # *   By default, if this parameter is not specified, a private IP address is randomly assigned from within the CIDR block of the specified vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

