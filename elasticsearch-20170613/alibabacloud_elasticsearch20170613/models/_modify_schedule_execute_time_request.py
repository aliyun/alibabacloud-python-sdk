# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScheduleExecuteTimeRequest(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        schedule_execute_time: str = None,
    ):
        self.event_id = event_id
        self.schedule_execute_time = schedule_execute_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.schedule_execute_time is not None:
            result['scheduleExecuteTime'] = self.schedule_execute_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('scheduleExecuteTime') is not None:
            self.schedule_execute_time = m.get('scheduleExecuteTime')

        return self

