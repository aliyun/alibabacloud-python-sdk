# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataAgentMetricsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        metric_names: str = None,
        metric_type: str = None,
        start_time: int = None,
    ):
        # The end time of the query range.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The metric names. Separate multiple names with commas (,).
        self.metric_names = metric_names
        # The metric type. Valid values:
        # - **basic**: basic metrics.
        # - **high_level**: advanced metrics.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # The start time of the query range.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_names is not None:
            result['MetricNames'] = self.metric_names

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricNames') is not None:
            self.metric_names = m.get('MetricNames')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

