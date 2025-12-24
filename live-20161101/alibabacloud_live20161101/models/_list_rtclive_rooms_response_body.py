# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListRTCLiveRoomsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rooms: List[str] = None,
        total: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.rooms = rooms
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rooms is not None:
            result['Rooms'] = self.rooms

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rooms') is not None:
            self.rooms = m.get('Rooms')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

