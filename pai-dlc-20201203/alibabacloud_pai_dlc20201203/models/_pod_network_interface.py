# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PodNetworkInterface(DaraModel):
    def __init__(
        self,
        interface_name: str = None,
        ip: str = None,
    ):
        self.interface_name = interface_name
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interface_name is not None:
            result['InterfaceName'] = self.interface_name

        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InterfaceName') is not None:
            self.interface_name = m.get('InterfaceName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

