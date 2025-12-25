# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubDomainInfo(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
        network_type: str = None,
        protocol: str = None,
    ):
        self.domain_id = domain_id
        self.name = name
        self.network_type = network_type
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.name is not None:
            result['name'] = self.name

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

