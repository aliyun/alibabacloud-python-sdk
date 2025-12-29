# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHotelSceneBookItemShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        update_hotel_scene_book_req_shrink: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # updateHotelSceneBookReq
        # 
        # This parameter is required.
        self.update_hotel_scene_book_req_shrink = update_hotel_scene_book_req_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.update_hotel_scene_book_req_shrink is not None:
            result['UpdateHotelSceneBookReq'] = self.update_hotel_scene_book_req_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('UpdateHotelSceneBookReq') is not None:
            self.update_hotel_scene_book_req_shrink = m.get('UpdateHotelSceneBookReq')

        return self

