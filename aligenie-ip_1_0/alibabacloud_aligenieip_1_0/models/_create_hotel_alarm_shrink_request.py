# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHotelAlarmShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        music_type: str = None,
        rooms_shrink: str = None,
        schedule_info_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.music_type = music_type
        # This parameter is required.
        self.rooms_shrink = rooms_shrink
        # This parameter is required.
        self.schedule_info_shrink = schedule_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.music_type is not None:
            result['MusicType'] = self.music_type

        if self.rooms_shrink is not None:
            result['Rooms'] = self.rooms_shrink

        if self.schedule_info_shrink is not None:
            result['ScheduleInfo'] = self.schedule_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')

        if m.get('Rooms') is not None:
            self.rooms_shrink = m.get('Rooms')

        if m.get('ScheduleInfo') is not None:
            self.schedule_info_shrink = m.get('ScheduleInfo')

        return self

