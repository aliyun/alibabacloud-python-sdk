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
        # Description.
        # 
        # - Must be 2 to 256 characters in length and can contain English or Chinese characters.
        # 
        # - Cannot start with http\\:// or https\\://.
        self.description = description
        self.enable_ipv_6 = enable_ipv_6
        self.ipv_6cidr_block = ipv_6cidr_block
        # vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # vSwitch name.
        # 
        # - Must be 2 to 128 characters long. Can contain letters, digits, Chinese characters, underscores (_), and hyphens (-).
        # 
        # - Must start with a letter or a Chinese character. Cannot start with http\\:// or https\\://.
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

