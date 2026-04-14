# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigSetRelationFromAddressRequest(DaraModel):
    def __init__(
        self,
        from_address: str = None,
        id: str = None,
    ):
        self.from_address = from_address
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_address is not None:
            result['FromAddress'] = self.from_address

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromAddress') is not None:
            self.from_address = m.get('FromAddress')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

