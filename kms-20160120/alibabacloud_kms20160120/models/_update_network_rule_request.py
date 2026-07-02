# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNetworkRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        source_private_ip: str = None,
    ):
        # The updated description.
        self.description = description
        # The name of the network control rule that you want to update.
        # 
        # This parameter is required.
        self.name = name
        # The updated private IP addresses or private CIDR blocks. Separate multiple IP addresses or private CIDR blocks with a comma (,).
        self.source_private_ip = source_private_ip

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourcePrivateIp') is not None:
            self.source_private_ip = m.get('SourcePrivateIp')

        return self

