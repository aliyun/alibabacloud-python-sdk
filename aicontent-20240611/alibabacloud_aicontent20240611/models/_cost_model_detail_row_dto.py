# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CostModelDetailRowDTO(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        values: str = None,
    ):
        self.timestamp = timestamp
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

