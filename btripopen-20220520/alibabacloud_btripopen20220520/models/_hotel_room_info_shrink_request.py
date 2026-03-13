# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelRoomInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        room_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.room_ids_shrink = room_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.room_ids_shrink is not None:
            result['room_ids'] = self.room_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('room_ids') is not None:
            self.room_ids_shrink = m.get('room_ids')

        return self

