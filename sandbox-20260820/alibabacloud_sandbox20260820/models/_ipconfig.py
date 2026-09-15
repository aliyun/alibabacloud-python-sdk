# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IPConfig(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip_address: str = None,
    ):
        self.description = description
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')

        return self

