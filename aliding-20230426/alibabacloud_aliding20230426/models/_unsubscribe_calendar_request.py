# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnsubscribeCalendarRequest(DaraModel):
    def __init__(
        self,
        calendar_id: str = None,
    ):
        # This parameter is required.
        self.calendar_id = calendar_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        return self

