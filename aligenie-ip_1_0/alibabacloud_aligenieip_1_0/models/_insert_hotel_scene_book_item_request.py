# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class InsertHotelSceneBookItemRequest(DaraModel):
    def __init__(
        self,
        add_hotel_scene_item_req: main_models.InsertHotelSceneBookItemRequestAddHotelSceneItemReq = None,
        hotel_id: str = None,
    ):
        # addHotelSceneItemReq
        # 
        # This parameter is required.
        self.add_hotel_scene_item_req = add_hotel_scene_item_req
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        if self.add_hotel_scene_item_req:
            self.add_hotel_scene_item_req.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_hotel_scene_item_req is not None:
            result['AddHotelSceneItemReq'] = self.add_hotel_scene_item_req.to_map()

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddHotelSceneItemReq') is not None:
            temp_model = main_models.InsertHotelSceneBookItemRequestAddHotelSceneItemReq()
            self.add_hotel_scene_item_req = temp_model.from_map(m.get('AddHotelSceneItemReq'))

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

class InsertHotelSceneBookItemRequestAddHotelSceneItemReq(DaraModel):
    def __init__(
        self,
        icon: str = None,
        name: str = None,
        price: int = None,
        type: str = None,
    ):
        # icon
        # 
        # This parameter is required.
        self.icon = icon
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.price = price
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['Icon'] = self.icon

        if self.name is not None:
            result['Name'] = self.name

        if self.price is not None:
            result['Price'] = self.price

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

