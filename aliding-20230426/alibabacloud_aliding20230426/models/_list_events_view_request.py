# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEventsViewRequest(DaraModel):
    def __init__(
        self,
        calendar_id: str = None,
        max_attendees: int = None,
        max_results: int = None,
        next_token: str = None,
        time_max: str = None,
        time_min: str = None,
    ):
        # This parameter is required.
        self.calendar_id = calendar_id
        self.max_attendees = max_attendees
        self.max_results = max_results
        self.next_token = next_token
        self.time_max = time_max
        self.time_min = time_min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        if self.max_attendees is not None:
            result['MaxAttendees'] = self.max_attendees

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.time_max is not None:
            result['TimeMax'] = self.time_max

        if self.time_min is not None:
            result['TimeMin'] = self.time_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('MaxAttendees') is not None:
            self.max_attendees = m.get('MaxAttendees')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TimeMax') is not None:
            self.time_max = m.get('TimeMax')

        if m.get('TimeMin') is not None:
            self.time_min = m.get('TimeMin')

        return self

