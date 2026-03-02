# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricData(DaraModel):
    def __init__(
        self,
        data: str = None,
        measures: str = None,
        metric: str = None,
        time: int = None,
        type: str = None,
        type_value: str = None,
    ):
        # This parameter is required.
        self.data = data
        # This parameter is required.
        self.measures = measures
        # This parameter is required.
        self.metric = metric
        # This parameter is required.
        self.time = time
        self.type = type
        self.type_value = type_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.measures is not None:
            result['measures'] = self.measures

        if self.metric is not None:
            result['metric'] = self.metric

        if self.time is not None:
            result['time'] = self.time

        if self.type is not None:
            result['type'] = self.type

        if self.type_value is not None:
            result['typeValue'] = self.type_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('measures') is not None:
            self.measures = m.get('measures')

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('typeValue') is not None:
            self.type_value = m.get('typeValue')

        return self

