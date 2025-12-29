# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRoomStatusRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
    ):
        self.hotel_id = hotel_id
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

