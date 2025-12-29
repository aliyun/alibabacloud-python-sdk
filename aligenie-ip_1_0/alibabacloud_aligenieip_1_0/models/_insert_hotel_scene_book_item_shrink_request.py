# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertHotelSceneBookItemShrinkRequest(DaraModel):
    def __init__(
        self,
        add_hotel_scene_item_req_shrink: str = None,
        hotel_id: str = None,
    ):
        # addHotelSceneItemReq
        # 
        # This parameter is required.
        self.add_hotel_scene_item_req_shrink = add_hotel_scene_item_req_shrink
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_hotel_scene_item_req_shrink is not None:
            result['AddHotelSceneItemReq'] = self.add_hotel_scene_item_req_shrink

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddHotelSceneItemReq') is not None:
            self.add_hotel_scene_item_req_shrink = m.get('AddHotelSceneItemReq')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

