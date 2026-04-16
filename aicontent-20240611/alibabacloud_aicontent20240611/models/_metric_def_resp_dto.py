# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricDefRespDTO(DaraModel):
    def __init__(
        self,
        key: str = None,
        label: str = None,
        sortable: bool = None,
        unit: str = None,
    ):
        self.key = key
        self.label = label
        self.sortable = sortable
        self.unit = unit

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

        if self.sortable is not None:
            result['sortable'] = self.sortable

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('sortable') is not None:
            self.sortable = m.get('sortable')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

