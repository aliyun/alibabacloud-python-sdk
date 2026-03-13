# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HotelRoomInfoRequest(DaraModel):
    def __init__(
        self,
        room_ids: List[int] = None,
    ):
        # This parameter is required.
        self.room_ids = room_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.room_ids is not None:
            result['room_ids'] = self.room_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('room_ids') is not None:
            self.room_ids = m.get('room_ids')

        return self

