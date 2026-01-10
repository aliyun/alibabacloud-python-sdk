# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateToolInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        schema: str = None,
    ):
        self.description = description
        self.name = name
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.schema is not None:
            result['schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        return self

