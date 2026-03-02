# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigModel(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        type: str = None,
        value: str = None,
    ):
        self.attribute = attribute
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

