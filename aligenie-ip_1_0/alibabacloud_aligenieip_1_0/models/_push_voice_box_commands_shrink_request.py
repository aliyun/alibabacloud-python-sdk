# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushVoiceBoxCommandsShrinkRequest(DaraModel):
    def __init__(
        self,
        commands_shrink: str = None,
        hotel_id: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.commands_shrink = commands_shrink
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
        if self.commands_shrink is not None:
            result['Commands'] = self.commands_shrink

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands_shrink = m.get('Commands')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

