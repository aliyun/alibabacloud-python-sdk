# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class KeywordSuggestInfo(DaraModel):
    def __init__(
        self,
        address: str = None,
        business_area_with_city: main_models.KeywordSuggestInfo = None,
        city_code: int = None,
        city_name: str = None,
        display_name: str = None,
        hotel_id: str = None,
        icon: str = None,
        point: str = None,
        price: str = None,
        region: int = None,
        type: int = None,
        type_desc: str = None,
    ):
        self.address = address
        self.business_area_with_city = business_area_with_city
        self.city_code = city_code
        self.city_name = city_name
        self.display_name = display_name
        self.hotel_id = hotel_id
        self.icon = icon
        self.point = point
        self.price = price
        self.region = region
        self.type = type
        self.type_desc = type_desc

    def validate(self):
        if self.business_area_with_city:
            self.business_area_with_city.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.business_area_with_city is not None:
            result['business_area_with_city'] = self.business_area_with_city.to_map()

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.display_name is not None:
            result['display_name'] = self.display_name

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.icon is not None:
            result['icon'] = self.icon

        if self.point is not None:
            result['point'] = self.point

        if self.price is not None:
            result['price'] = self.price

        if self.region is not None:
            result['region'] = self.region

        if self.type is not None:
            result['type'] = self.type

        if self.type_desc is not None:
            result['type_desc'] = self.type_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('business_area_with_city') is not None:
            temp_model = main_models.KeywordSuggestInfo()
            self.business_area_with_city = temp_model.from_map(m.get('business_area_with_city'))

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('point') is not None:
            self.point = m.get('point')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('type_desc') is not None:
            self.type_desc = m.get('type_desc')

        return self

