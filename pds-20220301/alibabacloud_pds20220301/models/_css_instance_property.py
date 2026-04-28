# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CssInstanceProperty(DaraModel):
    def __init__(
        self,
        code: str = None,
        global_key: str = None,
        name: str = None,
        unit: str = None,
        value: str = None,
    ):
        self.code = code
        self.global_key = global_key
        self.name = name
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.global_key is not None:
            result['globalKey'] = self.global_key

        if self.name is not None:
            result['name'] = self.name

        if self.unit is not None:
            result['unit'] = self.unit

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('globalKey') is not None:
            self.global_key = m.get('globalKey')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

