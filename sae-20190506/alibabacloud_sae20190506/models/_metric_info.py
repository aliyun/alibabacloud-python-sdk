# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricInfo(DaraModel):
    def __init__(
        self,
        average: float = None,
        count: float = None,
        maximum: float = None,
        minimum: float = None,
        sum: float = None,
        timestamp: int = None,
        value: float = None,
    ):
        self.average = average
        self.count = count
        self.maximum = maximum
        self.minimum = minimum
        self.sum = sum
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average is not None:
            result['Average'] = self.average

        if self.count is not None:
            result['Count'] = self.count

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        if self.minimum is not None:
            result['Minimum'] = self.minimum

        if self.sum is not None:
            result['Sum'] = self.sum

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')

        if m.get('Sum') is not None:
            self.sum = m.get('Sum')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

