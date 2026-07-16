# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        source_private_ip: str = None,
        type: str = None,
    ):
        # The description.
        self.description = description
        # The name of the access control rule.
        # 
        # This parameter is required.
        self.name = name
        # The private IP address or private CIDR block. Separate multiple items with commas (,).
        self.source_private_ip = source_private_ip
        # The network type.
        # 
        # Only private IP addresses are supported. Set the value to Private.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.source_private_ip is not None:
            result['SourcePrivateIp'] = self.source_private_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourcePrivateIp') is not None:
            self.source_private_ip = m.get('SourcePrivateIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

