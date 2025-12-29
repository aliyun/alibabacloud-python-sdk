# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SchemaTablesValueFieldsValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        primary_key: bool = None,
        type: str = None,
        join_with: List[str] = None,
        label: str = None,
    ):
        self.name = name
        self.primary_key = primary_key
        self.type = type
        self.join_with = join_with
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key

        if self.type is not None:
            result['type'] = self.type

        if self.join_with is not None:
            result['joinWith'] = self.join_with

        if self.label is not None:
            result['label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('joinWith') is not None:
            self.join_with = m.get('joinWith')

        if m.get('label') is not None:
            self.label = m.get('label')

        return self

