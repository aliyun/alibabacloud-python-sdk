# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAccountAddressInfoWithoutHavanaRequest(DaraModel):
    def __init__(
        self,
        address_version: str = None,
        havana_id: str = None,
        pk: str = None,
    ):
        self.address_version = address_version
        self.havana_id = havana_id
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_version is not None:
            result['AddressVersion'] = self.address_version

        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id

        if self.pk is not None:
            result['PK'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressVersion') is not None:
            self.address_version = m.get('AddressVersion')

        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        return self

