# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DateSummary(DaraModel):
    def __init__(
        self,
        date: str = None,
        value: int = None,
    ):
        self.date = date
        # Metric value at corresponding date
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

