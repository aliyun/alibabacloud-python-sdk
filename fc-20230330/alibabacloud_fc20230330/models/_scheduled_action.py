# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduledAction(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_expression: str = None,
        start_time: str = None,
        target: int = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schedule_expression = schedule_expression
        self.start_time = start_time
        # This parameter is required.
        self.target = target
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

