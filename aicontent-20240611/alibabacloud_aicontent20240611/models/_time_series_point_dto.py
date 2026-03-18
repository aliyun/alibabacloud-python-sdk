# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class TimeSeriesPointDTO(DaraModel):
    def __init__(
        self,
        label: str = None,
        timestamp: str = None,
        value: Any = None,
    ):
        self.label = label
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['label'] = self.label

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

