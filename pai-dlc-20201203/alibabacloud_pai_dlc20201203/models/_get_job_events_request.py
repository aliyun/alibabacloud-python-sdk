# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_events_num: int = None,
        start_time: str = None,
    ):
        # The end time (UTC) of the time range for querying events. The default value is the current time.
        self.end_time = end_time
        # The maximum number of events that can be returned. Default value: 2000.
        self.max_events_num = max_events_num
        # The start time (UTC) of the time range for querying events. The default value is 7 days ago.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

