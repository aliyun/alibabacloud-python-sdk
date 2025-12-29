# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelsRequest(DaraModel):
    def __init__(
        self,
        hotel_request: main_models.ListHotelsRequestHotelRequest = None,
        page: main_models.ListHotelsRequestPage = None,
        status: int = None,
    ):
        self.hotel_request = hotel_request
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.hotel_request:
            self.hotel_request.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_request is not None:
            result['HotelRequest'] = self.hotel_request.to_map()

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelRequest') is not None:
            temp_model = main_models.ListHotelsRequestHotelRequest()
            self.hotel_request = temp_model.from_map(m.get('HotelRequest'))

        if m.get('Page') is not None:
            temp_model = main_models.ListHotelsRequestPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListHotelsRequestPage(DaraModel):
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

class ListHotelsRequestHotelRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
    ):
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

