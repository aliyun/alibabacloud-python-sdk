# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricValueDTO(DaraModel):
    def __init__(
        self,
        key: str = None,
        label: str = None,
        unit: str = None,
        value: float = None,
    ):
        self.key = key
        self.label = label
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.label is not None:
            result['label'] = self.label

        if self.unit is not None:
            result['unit'] = self.unit

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

