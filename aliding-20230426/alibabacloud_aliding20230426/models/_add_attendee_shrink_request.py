# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAttendeeShrinkRequest(DaraModel):
    def __init__(
        self,
        attendees_to_add_shrink: str = None,
        calendar_id: str = None,
        event_id: str = None,
        chat_notification: bool = None,
        push_notification: bool = None,
    ):
        # This parameter is required.
        self.attendees_to_add_shrink = attendees_to_add_shrink
        # This parameter is required.
        self.calendar_id = calendar_id
        # This parameter is required.
        self.event_id = event_id
        self.chat_notification = chat_notification
        self.push_notification = push_notification

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attendees_to_add_shrink is not None:
            result['AttendeesToAdd'] = self.attendees_to_add_shrink

        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.chat_notification is not None:
            result['chatNotification'] = self.chat_notification

        if self.push_notification is not None:
            result['pushNotification'] = self.push_notification

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttendeesToAdd') is not None:
            self.attendees_to_add_shrink = m.get('AttendeesToAdd')

        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('chatNotification') is not None:
            self.chat_notification = m.get('chatNotification')

        if m.get('pushNotification') is not None:
            self.push_notification = m.get('pushNotification')

        return self

