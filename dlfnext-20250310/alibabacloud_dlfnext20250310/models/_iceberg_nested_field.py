# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class IcebergNestedField(DaraModel):
    def __init__(
        self,
        doc: str = None,
        id: int = None,
        name: str = None,
        optional: bool = None,
        type: str = None,
    ):
        self.doc = doc
        self.id = id
        self.name = name
        self.optional = optional
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc is not None:
            result['doc'] = self.doc

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.optional is not None:
            result['optional'] = self.optional

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('doc') is not None:
            self.doc = m.get('doc')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('optional') is not None:
            self.optional = m.get('optional')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

