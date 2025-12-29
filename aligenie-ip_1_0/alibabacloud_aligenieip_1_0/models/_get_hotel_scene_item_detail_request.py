# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotelSceneItemDetailRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        item_id: int = None,
        name: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        self.item_id = item_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

