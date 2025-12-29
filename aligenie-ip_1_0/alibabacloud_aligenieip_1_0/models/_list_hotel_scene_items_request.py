# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelSceneItemsRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        list_hotel_scene_req: main_models.ListHotelSceneItemsRequestListHotelSceneReq = None,
    ):
        # hotelID
        # 
        # This parameter is required.
        self.hotel_id = hotel_id
        # ListHotelSceneReq
        # 
        # This parameter is required.
        self.list_hotel_scene_req = list_hotel_scene_req

    def validate(self):
        if self.list_hotel_scene_req:
            self.list_hotel_scene_req.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.list_hotel_scene_req is not None:
            result['ListHotelSceneReq'] = self.list_hotel_scene_req.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('ListHotelSceneReq') is not None:
            temp_model = main_models.ListHotelSceneItemsRequestListHotelSceneReq()
            self.list_hotel_scene_req = temp_model.from_map(m.get('ListHotelSceneReq'))

        return self

class ListHotelSceneItemsRequestListHotelSceneReq(DaraModel):
    def __init__(
        self,
        category: str = None,
        keywords: str = None,
        page: main_models.ListHotelSceneItemsRequestListHotelSceneReqPage = None,
        status: str = None,
        type: str = None,
    ):
        self.category = category
        self.keywords = keywords
        # This parameter is required.
        self.page = page
        self.status = status
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
        if self.category is not None:
            result['Category'] = self.category

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Page') is not None:
            temp_model = main_models.ListHotelSceneItemsRequestListHotelSceneReqPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListHotelSceneItemsRequestListHotelSceneReqPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
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

