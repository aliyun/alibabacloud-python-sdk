# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class UpdateHotelSceneBookItemRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        update_hotel_scene_book_req: main_models.UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # updateHotelSceneBookReq
        # 
        # This parameter is required.
        self.update_hotel_scene_book_req = update_hotel_scene_book_req

    def validate(self):
        if self.update_hotel_scene_book_req:
            self.update_hotel_scene_book_req.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.update_hotel_scene_book_req is not None:
            result['UpdateHotelSceneBookReq'] = self.update_hotel_scene_book_req.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('UpdateHotelSceneBookReq') is not None:
            temp_model = main_models.UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq()
            self.update_hotel_scene_book_req = temp_model.from_map(m.get('UpdateHotelSceneBookReq'))

        return self

class UpdateHotelSceneBookItemRequestUpdateHotelSceneBookReq(DaraModel):
    def __init__(
        self,
        icon: str = None,
        id: int = None,
        name: str = None,
        price: int = None,
    ):
        # icon
        # 
        # This parameter is required.
        self.icon = icon
        self.id = id
        self.name = name
        # This parameter is required.
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.price is not None:
            result['Price'] = self.price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        return self

