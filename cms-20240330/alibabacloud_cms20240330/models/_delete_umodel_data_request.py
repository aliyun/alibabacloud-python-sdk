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
        # Can specify the name of a specific Umodel data, leaving it blank means all
        self.domain = domain
        # Can specify the kind of a specific Umodel data, leaving it blank means all
        self.kind = kind
        # Can specify the name of a specific Umodel data, leaving it blank means all
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

