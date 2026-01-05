# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class QueryInstanceMetricsRequest(DaraModel):
    def __init__(
        self,
        dimensions: Dict[str, Any] = None,
        end_time: str = None,
        metric_type: str = None,
        start_time: str = None,
        time_step: str = None,
    ):
        self.dimensions = dimensions
        self.end_time = end_time
        # This parameter is required.
        self.metric_type = metric_type
        self.start_time = start_time
        self.time_step = time_step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_step is not None:
            result['TimeStep'] = self.time_step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')

        return self

