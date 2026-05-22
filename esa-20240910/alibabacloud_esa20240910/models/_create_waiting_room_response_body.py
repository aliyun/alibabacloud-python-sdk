# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWaitingRoomResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        waiting_room_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.waiting_room_id = waiting_room_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')

        return self

