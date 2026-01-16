# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncTaskEvent(DaraModel):
    def __init__(
        self,
        event_detail: str = None,
        event_id: int = None,
        status: str = None,
        timestamp: int = None,
    ):
        self.event_detail = event_detail
        self.event_id = event_id
        self.status = status
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_detail is not None:
            result['eventDetail'] = self.event_detail

        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.status is not None:
            result['status'] = self.status

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventDetail') is not None:
            self.event_detail = m.get('eventDetail')

        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

