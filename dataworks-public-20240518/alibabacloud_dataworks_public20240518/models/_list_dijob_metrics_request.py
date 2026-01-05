# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDIJobMetricsRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        end_time: int = None,
        metric_name: List[str] = None,
        start_time: int = None,
    ):
        # The ID of the synchronization task.
        self.dijob_id = dijob_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The metrics that you want to query.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The beginning of the time range to query.
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
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

