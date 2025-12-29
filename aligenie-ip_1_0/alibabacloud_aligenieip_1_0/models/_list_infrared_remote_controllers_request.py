# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInfraredRemoteControllersRequest(DaraModel):
    def __init__(
        self,
        brand: str = None,
        category: str = None,
        city: str = None,
        hotel_id: str = None,
        province: str = None,
        service_provider: str = None,
    ):
        self.brand = brand
        # This parameter is required.
        self.category = category
        self.city = city
        # This parameter is required.
        self.hotel_id = hotel_id
        self.province = province
        self.service_provider = service_provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand is not None:
            result['Brand'] = self.brand

        if self.category is not None:
            result['Category'] = self.category

        if self.city is not None:
            result['City'] = self.city

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.province is not None:
            result['Province'] = self.province

        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')

        return self

