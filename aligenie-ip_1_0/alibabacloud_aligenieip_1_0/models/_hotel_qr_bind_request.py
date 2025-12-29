# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelQrBindRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        code: str = None,
        ext_info: str = None,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        # This parameter is required.
        self.code = code
        self.ext_info = ext_info
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.code is not None:
            result['Code'] = self.code

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

