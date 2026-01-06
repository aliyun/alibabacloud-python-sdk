# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class RemoveMeetingRoomsRequest(DaraModel):
    def __init__(
        self,
        calendar_id: str = None,
        event_id: str = None,
        meeting_rooms_to_remove: List[main_models.RemoveMeetingRoomsRequestMeetingRoomsToRemove] = None,
    ):
        # This parameter is required.
        self.calendar_id = calendar_id
        # This parameter is required.
        self.event_id = event_id
        self.meeting_rooms_to_remove = meeting_rooms_to_remove

    def validate(self):
        if self.meeting_rooms_to_remove:
            for v1 in self.meeting_rooms_to_remove:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        result['MeetingRoomsToRemove'] = []
        if self.meeting_rooms_to_remove is not None:
            for k1 in self.meeting_rooms_to_remove:
                result['MeetingRoomsToRemove'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        self.meeting_rooms_to_remove = []
        if m.get('MeetingRoomsToRemove') is not None:
            for k1 in m.get('MeetingRoomsToRemove'):
                temp_model = main_models.RemoveMeetingRoomsRequestMeetingRoomsToRemove()
                self.meeting_rooms_to_remove.append(temp_model.from_map(k1))

        return self

class RemoveMeetingRoomsRequestMeetingRoomsToRemove(DaraModel):
    def __init__(
        self,
        room_id: str = None,
    ):
        # This parameter is required.
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.room_id is not None:
            result['RoomId'] = self.room_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')

        return self

