# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEventRequest(DaraModel):
    def __init__(
        self,
        calendar_id: str = None,
        event_id: str = None,
        max_attendees: int = None,
    ):
        # This parameter is required.
        self.calendar_id = calendar_id
        # This parameter is required.
        self.event_id = event_id
        self.max_attendees = max_attendees

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.max_attendees is not None:
            result['MaxAttendees'] = self.max_attendees

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('MaxAttendees') is not None:
            self.max_attendees = m.get('MaxAttendees')

        return self

