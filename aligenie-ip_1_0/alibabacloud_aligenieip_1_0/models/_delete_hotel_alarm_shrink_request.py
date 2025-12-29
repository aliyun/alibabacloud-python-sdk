# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHotelAlarmShrinkRequest(DaraModel):
    def __init__(
        self,
        alarms_shrink: str = None,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.alarms_shrink = alarms_shrink
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarms_shrink is not None:
            result['Alarms'] = self.alarms_shrink

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarms') is not None:
            self.alarms_shrink = m.get('Alarms')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

