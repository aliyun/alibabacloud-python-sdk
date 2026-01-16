# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TargetTrackingPolicy(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_capacity: int = None,
        metric_target: float = None,
        metric_type: str = None,
        min_capacity: int = None,
        name: str = None,
        start_time: str = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.max_capacity = max_capacity
        # This parameter is required.
        self.metric_target = metric_target
        # This parameter is required.
        self.metric_type = metric_type
        # This parameter is required.
        self.min_capacity = min_capacity
        # This parameter is required.
        self.name = name
        self.start_time = start_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.max_capacity is not None:
            result['maxCapacity'] = self.max_capacity

        if self.metric_target is not None:
            result['metricTarget'] = self.metric_target

        if self.metric_type is not None:
            result['metricType'] = self.metric_type

        if self.min_capacity is not None:
            result['minCapacity'] = self.min_capacity

        if self.name is not None:
            result['name'] = self.name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('maxCapacity') is not None:
            self.max_capacity = m.get('maxCapacity')

        if m.get('metricTarget') is not None:
            self.metric_target = m.get('metricTarget')

        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')

        if m.get('minCapacity') is not None:
            self.min_capacity = m.get('minCapacity')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

