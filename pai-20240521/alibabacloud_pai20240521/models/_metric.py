# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Metric(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

