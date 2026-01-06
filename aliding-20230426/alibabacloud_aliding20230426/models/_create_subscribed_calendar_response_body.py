# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSubscribedCalendarResponseBody(DaraModel):
    def __init__(
        self,
        calendar_id: str = None,
        request_id: str = None,
    ):
        self.calendar_id = calendar_id
        # requestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_id is not None:
            result['calendarId'] = self.calendar_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('calendarId') is not None:
            self.calendar_id = m.get('calendarId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

