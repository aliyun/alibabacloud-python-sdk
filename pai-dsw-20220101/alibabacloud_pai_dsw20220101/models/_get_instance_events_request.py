# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_level: str = None,
        max_events_num: int = None,
        start_time: str = None,
        token: str = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        self.event_level = event_level
        # The maximum number of events. Default value: 2000.
        self.max_events_num = max_events_num
        # The beginning of the time range to query.
        self.start_time = start_time
        # The token used to share the URL.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

