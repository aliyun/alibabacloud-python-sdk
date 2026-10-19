# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVSwitchAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        enable_ipv_6: bool = None,
        ipv_6cidr_block: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # The description.
        # 
        # - The description must be 2 to 256 characters in length.
        # - It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to enable IPv6 for the vSwitch. Valid values:
        # - true: enables IPv6. The VPC to which the vSwitch belongs must have IPv6 enabled, and you must also specify Ipv6CidrBlock to assign an IPv6 CIDR block to the vSwitch.
        # - false (default): disables IPv6. Before you disable IPv6 for the vSwitch, make sure that no IPv6 addresses are in use, and do not specify Ipv6CidrBlock at the same time.
        self.enable_ipv_6 = enable_ipv_6
        # The IPv6 CIDR block of the vSwitch.
        # 
        # > You can specify this parameter to assign an IPv6 CIDR block to the vSwitch only when IPv6 is enabled for the VPC to which the vSwitch belongs. After the IPv6 CIDR block is assigned, it cannot be changed. Make sure that the IPv6 CIDR block does not overlap with the CIDR blocks of other vSwitches in the same VPC.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The vSwitch name.
        # 
        # - The name must be 2 to 128 characters in length.
        # - It must start with a letter or a Chinese character and cannot start with http:// or https://.
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.enable_ipv_6 is not None:
            result['EnableIPv6'] = self.enable_ipv_6

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableIPv6') is not None:
            self.enable_ipv_6 = m.get('EnableIPv6')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

