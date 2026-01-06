# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class AddAttendeeRequest(DaraModel):
    def __init__(
        self,
        attendees_to_add: List[main_models.AddAttendeeRequestAttendeesToAdd] = None,
        calendar_id: str = None,
        event_id: str = None,
        chat_notification: bool = None,
        push_notification: bool = None,
    ):
        # This parameter is required.
        self.attendees_to_add = attendees_to_add
        # This parameter is required.
        self.calendar_id = calendar_id
        # This parameter is required.
        self.event_id = event_id
        self.chat_notification = chat_notification
        self.push_notification = push_notification

    def validate(self):
        if self.attendees_to_add:
            for v1 in self.attendees_to_add:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttendeesToAdd'] = []
        if self.attendees_to_add is not None:
            for k1 in self.attendees_to_add:
                result['AttendeesToAdd'].append(k1.to_map() if k1 else None)

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
        self.attendees_to_add = []
        if m.get('AttendeesToAdd') is not None:
            for k1 in m.get('AttendeesToAdd'):
                temp_model = main_models.AddAttendeeRequestAttendeesToAdd()
                self.attendees_to_add.append(temp_model.from_map(k1))

        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('chatNotification') is not None:
            self.chat_notification = m.get('chatNotification')

        if m.get('pushNotification') is not None:
            self.push_notification = m.get('pushNotification')

        return self

class AddAttendeeRequestAttendeesToAdd(DaraModel):
    def __init__(
        self,
        id: str = None,
        is_optional: bool = None,
    ):
        self.id = id
        self.is_optional = is_optional

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.is_optional is not None:
            result['isOptional'] = self.is_optional

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isOptional') is not None:
            self.is_optional = m.get('isOptional')

        return self

