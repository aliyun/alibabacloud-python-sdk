# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricListRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        end_time: int = None,
        instance: str = None,
        metric_name: str = None,
        start_time: int = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The end time, in seconds (UNIX timestamp).
        self.end_time = end_time
        # The instance ID.
        self.instance = instance
        # The metric name.
        self.metric_name = metric_name
        # The start time, in seconds (UNIX timestamp).
        self.start_time = start_time
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.instance is not None:
            result['instance'] = self.instance

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

