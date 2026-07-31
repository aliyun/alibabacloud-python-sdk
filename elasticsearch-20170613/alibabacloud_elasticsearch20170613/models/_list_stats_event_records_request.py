# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStatsEventRecordsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        event_type: str = None,
        level: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.end_time = end_time
        # The event type.
        self.event_type = event_type
        # The event level.
        self.level = level
        self.start_time = start_time
        # The event status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.level is not None:
            result['level'] = self.level

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

