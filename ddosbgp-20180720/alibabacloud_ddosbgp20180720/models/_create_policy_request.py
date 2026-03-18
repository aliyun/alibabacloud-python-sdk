# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        port_version: str = None,
        type: str = None,
    ):
        # The name of the policy.
        # 
        # This parameter is required.
        self.name = name
        self.port_version = port_version
        # The type of the policy. Valid values:
        # 
        # *   **l3**: IP-specific mitigation policies.
        # *   **l4**: port-specific mitigation policies.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

