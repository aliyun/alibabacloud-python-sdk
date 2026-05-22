# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWaitingRoomEventResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_room_event_id: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.waiting_room_event_id = waiting_room_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')

        return self

