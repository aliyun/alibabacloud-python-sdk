# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricListRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance: str = None,
        metric_name: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance = instance
        self.metric_name = metric_name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.instance is not None:
            result['instance'] = self.instance

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

