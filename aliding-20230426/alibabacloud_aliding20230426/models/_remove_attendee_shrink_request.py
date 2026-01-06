# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveAttendeeShrinkRequest(DaraModel):
    def __init__(
        self,
        attendees_to_remove_shrink: str = None,
        calendar_id: str = None,
        event_id: str = None,
    ):
        self.attendees_to_remove_shrink = attendees_to_remove_shrink
        # This parameter is required.
        self.calendar_id = calendar_id
        # This parameter is required.
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attendees_to_remove_shrink is not None:
            result['AttendeesToRemove'] = self.attendees_to_remove_shrink

        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttendeesToRemove') is not None:
            self.attendees_to_remove_shrink = m.get('AttendeesToRemove')

        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        return self

