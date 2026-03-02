# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RuleCondition(DaraModel):
    def __init__(
        self,
        name: str = None,
        position: str = None,
        relation: str = None,
        value: str = None,
        value_type: str = None,
    ):
        self.name = name
        self.position = position
        self.relation = relation
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.position is not None:
            result['position'] = self.position

        if self.relation is not None:
            result['relation'] = self.relation

        if self.value is not None:
            result['value'] = self.value

        if self.value_type is not None:
            result['valueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')

        return self

