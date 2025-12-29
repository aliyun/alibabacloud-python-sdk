# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotelSceneBookItemsShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        page_shrink: str = None,
        type: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.page_shrink = page_shrink
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.page_shrink is not None:
            result['Page'] = self.page_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

