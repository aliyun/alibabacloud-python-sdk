# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListJobMetricRequest(DaraModel):
    def __init__(
        self,
        group: str = None,
        metric: str = None,
        period: int = None,
        project: List[str] = None,
        quota: List[str] = None,
        type: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # The grouping basis.
        # 
        # > Valid values:
        # > - project: grouping and aggregation by project
        # > - quota: grouping and aggregation by quota
        # > - type: grouping and aggregation by job type
        # > - status: grouping and aggregation by job status
        self.group = group
        # The metric information.
        self.metric = metric
        # The monitoring statistical period.
        self.period = period
        # The list of MaxCompute project names used for filtering.
        self.project = project
        # The list of compute quota nicknames used for filtering.
        self.quota = quota
        # The metric type.
        self.type = type
        # The end time of the query time range. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start time of the query time range. The value is a UNIX timestamp in seconds.
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
        if self.group is not None:
            result['group'] = self.group

        if self.metric is not None:
            result['metric'] = self.metric

        if self.period is not None:
            result['period'] = self.period

        if self.project is not None:
            result['project'] = self.project

        if self.quota is not None:
            result['quota'] = self.quota

        if self.type is not None:
            result['type'] = self.type

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('quota') is not None:
            self.quota = m.get('quota')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

