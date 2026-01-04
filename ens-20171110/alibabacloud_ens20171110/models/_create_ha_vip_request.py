# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHaVipRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        description: str = None,
        ip_address: str = None,
        name: str = None,
        v_switch_id: str = None,
    ):
        # The number of HAVIPs that you want to create. Valid values: 1 to 10. The value can be only 1 if you specify an IP address.
        # 
        # Default value: 1.
        self.amount = amount
        # The description of the HAVIP.
        self.description = description
        # The IP address of the HAVIP.
        self.ip_address = ip_address
        # The name of the HAVIP.
        self.name = name
        # The vSwitch ID of the HAVIP.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

