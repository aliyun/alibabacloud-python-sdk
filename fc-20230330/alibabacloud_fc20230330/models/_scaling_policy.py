# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScalingPolicy(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_instances: int = None,
        metric_target: float = None,
        metric_type: str = None,
        min_instances: int = None,
        name: str = None,
        start_time: str = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.max_instances = max_instances
        self.metric_target = metric_target
        self.metric_type = metric_type
        self.min_instances = min_instances
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

        if self.max_instances is not None:
            result['maxInstances'] = self.max_instances

        if self.metric_target is not None:
            result['metricTarget'] = self.metric_target

        if self.metric_type is not None:
            result['metricType'] = self.metric_type

        if self.min_instances is not None:
            result['minInstances'] = self.min_instances

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

        if m.get('maxInstances') is not None:
            self.max_instances = m.get('maxInstances')

        if m.get('metricTarget') is not None:
            self.metric_target = m.get('metricTarget')

        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')

        if m.get('minInstances') is not None:
            self.min_instances = m.get('minInstances')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

