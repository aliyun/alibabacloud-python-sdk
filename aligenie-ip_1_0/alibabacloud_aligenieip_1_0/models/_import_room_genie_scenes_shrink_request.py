# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportRoomGenieScenesShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        room_no: str = None,
        scene_list_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.room_no = room_no
        self.scene_list_shrink = scene_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.scene_list_shrink is not None:
            result['SceneList'] = self.scene_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('SceneList') is not None:
            self.scene_list_shrink = m.get('SceneList')

        return self

