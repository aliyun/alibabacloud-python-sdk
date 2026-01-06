# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetMeetingRoomsScheduleRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        room_ids: List[str] = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.room_ids = room_ids
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.room_ids is not None:
            result['RoomIds'] = self.room_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RoomIds') is not None:
            self.room_ids = m.get('RoomIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

