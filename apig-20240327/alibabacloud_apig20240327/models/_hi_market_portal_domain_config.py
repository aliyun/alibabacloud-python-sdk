# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketPortalDomainConfig(DaraModel):
    def __init__(
        self,
        domain: str = None,
        protocol: str = None,
        type: str = None,
    ):
        self.domain = domain
        self.protocol = protocol
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

