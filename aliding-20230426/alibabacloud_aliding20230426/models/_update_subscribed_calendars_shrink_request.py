# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubscribedCalendarsShrinkRequest(DaraModel):
    def __init__(
        self,
        calendar_id: str = None,
        description: str = None,
        managers_shrink: str = None,
        name: str = None,
        subscribe_scope_shrink: str = None,
    ):
        # This parameter is required.
        self.calendar_id = calendar_id
        self.description = description
        self.managers_shrink = managers_shrink
        self.name = name
        self.subscribe_scope_shrink = subscribe_scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        if self.description is not None:
            result['Description'] = self.description

        if self.managers_shrink is not None:
            result['Managers'] = self.managers_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.subscribe_scope_shrink is not None:
            result['SubscribeScope'] = self.subscribe_scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Managers') is not None:
            self.managers_shrink = m.get('Managers')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SubscribeScope') is not None:
            self.subscribe_scope_shrink = m.get('SubscribeScope')

        return self

