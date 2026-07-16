# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUmodelDataRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        kind: str = None,
        name: str = None,
    ):
        # The name of the Umodel data to delete. Omit this parameter to delete all Umodel data.
        self.domain = domain
        # The kind of the Umodel data. If unspecified, data of all kinds is deleted.
        self.kind = kind
        # The name of the Umodel data. If unspecified, data with any name is deleted.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

