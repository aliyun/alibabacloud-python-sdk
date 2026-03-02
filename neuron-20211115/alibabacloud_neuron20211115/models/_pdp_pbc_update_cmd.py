# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpPbcUpdateCmd(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.alias = alias
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

