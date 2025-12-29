# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelRoomsRequest(DaraModel):
    def __init__(
        self,
        hotel_admin_room: main_models.ListHotelRoomsRequestHotelAdminRoom = None,
        hotel_id: str = None,
    ):
        self.hotel_admin_room = hotel_admin_room
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        if self.hotel_admin_room:
            self.hotel_admin_room.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_admin_room is not None:
            result['HotelAdminRoom'] = self.hotel_admin_room.to_map()

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelAdminRoom') is not None:
            temp_model = main_models.ListHotelRoomsRequestHotelAdminRoom()
            self.hotel_admin_room = temp_model.from_map(m.get('HotelAdminRoom'))

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

class ListHotelRoomsRequestHotelAdminRoom(DaraModel):
    def __init__(
        self,
        room_no: str = None,
    ):
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

