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
        # The ENS instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new private IP address.
        # Default value: If this parameter is not specified, an IP address is randomly assigned from the CIDR block of the vSwitch.
        self.private_ip_address = private_ip_address
        # The vSwitch ID.
        # - If the specified ID is the current vSwitch of the instance, the vSwitch of the instance remains unchanged.
        # - If the specified ID is a new vSwitch, the new and old vSwitches must belong to the same edge zone.
        # - If this parameter is not specified, a value is randomly assigned from the CIDR block of the original vSwitch.
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

