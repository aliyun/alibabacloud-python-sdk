# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveMeetingRoomsShrinkRequest(DaraModel):
    def __init__(
        self,
        calendar_id: str = None,
        event_id: str = None,
        meeting_rooms_to_remove_shrink: str = None,
    ):
        # This parameter is required.
        self.calendar_id = calendar_id
        # This parameter is required.
        self.event_id = event_id
        self.meeting_rooms_to_remove_shrink = meeting_rooms_to_remove_shrink

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

        if self.meeting_rooms_to_remove_shrink is not None:
            result['MeetingRoomsToRemove'] = self.meeting_rooms_to_remove_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('MeetingRoomsToRemove') is not None:
            self.meeting_rooms_to_remove_shrink = m.get('MeetingRoomsToRemove')

        return self

