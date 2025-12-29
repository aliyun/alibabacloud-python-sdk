# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelSceneBookItemsRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        page: main_models.ListHotelSceneBookItemsRequestPage = None,
        type: str = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Page') is not None:
            temp_model = main_models.ListHotelSceneBookItemsRequestPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListHotelSceneBookItemsRequestPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

