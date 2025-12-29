# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvokeRobotPushRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        push_type: str = None,
        room_name: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.push_type = push_type
        self.room_name = room_name
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

        if self.push_type is not None:
            result['PushType'] = self.push_type

        if self.room_name is not None:
            result['RoomName'] = self.room_name

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')

        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

