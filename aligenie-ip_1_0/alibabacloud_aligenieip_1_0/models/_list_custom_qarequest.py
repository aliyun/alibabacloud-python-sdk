# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListCustomQARequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        keyword: str = None,
        page: main_models.ListCustomQARequestPage = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        self.keyword = keyword
        # This parameter is required.
        self.page = page

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

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page is not None:
            result['Page'] = self.page.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Page') is not None:
            temp_model = main_models.ListCustomQARequestPage()
            self.page = temp_model.from_map(m.get('Page'))

        return self

class ListCustomQARequestPage(DaraModel):
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

