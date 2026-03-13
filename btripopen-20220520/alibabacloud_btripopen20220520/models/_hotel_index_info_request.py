# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HotelIndexInfoRequest(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        hotel_status: int = None,
        page_size: int = None,
        page_token: str = None,
    ):
        self.city_code = city_code
        self.hotel_status = hotel_status
        # This parameter is required.
        self.page_size = page_size
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.hotel_status is not None:
            result['hotel_status'] = self.hotel_status

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.page_token is not None:
            result['page_token'] = self.page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('hotel_status') is not None:
            self.hotel_status = m.get('hotel_status')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')

        return self

