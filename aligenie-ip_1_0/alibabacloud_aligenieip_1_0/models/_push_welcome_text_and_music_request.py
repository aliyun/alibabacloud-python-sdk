# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class PushWelcomeTextAndMusicRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_name: str = None,
        room_no: str = None,
        template_variable: Dict[str, str] = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.room_name = room_name
        self.room_no = room_no
        self.template_variable = template_variable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.room_name is not None:
            result['RoomName'] = self.room_name

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.template_variable is not None:
            result['TemplateVariable'] = self.template_variable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('TemplateVariable') is not None:
            self.template_variable = m.get('TemplateVariable')

        return self

