# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class ModelParameterRule(DaraModel):
    def __init__(
        self,
        default: Any = None,
        max: int = None,
        min: int = None,
        name: str = None,
        required: bool = None,
        type: str = None,
    ):
        self.default = default
        self.max = max
        self.min = min
        self.name = name
        self.required = required
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['default'] = self.default

        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        if self.name is not None:
            result['name'] = self.name

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

