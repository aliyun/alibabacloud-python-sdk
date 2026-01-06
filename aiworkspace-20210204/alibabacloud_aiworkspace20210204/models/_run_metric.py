# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunMetric(DaraModel):
    def __init__(
        self,
        key: str = None,
        step: int = None,
        timestamp: int = None,
        value: float = None,
    ):
        # This parameter is required.
        self.key = key
        self.step = step
        self.timestamp = timestamp
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.step is not None:
            result['Step'] = self.step

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

