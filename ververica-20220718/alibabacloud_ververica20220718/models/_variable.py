# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Variable(DaraModel):
    def __init__(
        self,
        description: str = None,
        kind: str = None,
        name: str = None,
        value: str = None,
    ):
        # The description of the variable.
        self.description = description
        # The type of the variable. Valid value: Plain.
        # 
        # This parameter is required.
        self.kind = kind
        # The name of the variable.
        # 
        # This parameter is required.
        self.name = name
        # The value of the variable.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

