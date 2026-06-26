# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduledPolicy(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The policy name.
        self.name = name
        # The schedule configuration.
        self.schedule_expression = schedule_expression
        # The start time.
        self.start_time = start_time
        # The current number of target resources. If a metric-based auto scaling policy or a scheduled policy is in effect, this parameter specifies the number of resources calculated by the policy. Otherwise, this parameter specifies the default number of provisioned instances.
        # 
        # > How is this different from defaultTarget?<br>
        # > Assume that you set the number of provisioned instances to 1 and then add a scheduled auto scaling policy to set the number to 5 for a specific time period.<br>
        # >
        # > - When the scheduled policy is active, target is 5 and defaultTarget is 1.
        # >
        # > - When the scheduled policy is inactive, both target and defaultTarget are 1.
        self.target = target
        # The time zone. If this parameter is left empty, the times for startTime, endTime, and scheduleExpression must be in UTC format.
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

        if self.name is not None:
            result['name'] = self.name

        if self.schedule_expression is not None:
            result['scheduleExpression'] = self.schedule_expression

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.target is not None:
            result['target'] = self.target

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduleExpression') is not None:
            self.schedule_expression = m.get('scheduleExpression')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

