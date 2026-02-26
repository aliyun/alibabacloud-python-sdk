# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddressForStory(DaraModel):
    def __init__(
        self,
        city: str = None,
        country: str = None,
        district: str = None,
        province: str = None,
        township: str = None,
    ):
        # The city.
        self.city = city
        # The country.
        self.country = country
        # The district.
        self.district = district
        # The province.
        self.province = province
        # The township.
        self.township = township

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.district is not None:
            result['District'] = self.district

        if self.province is not None:
            result['Province'] = self.province

        if self.township is not None:
            result['Township'] = self.township

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('District') is not None:
            self.district = m.get('District')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('Township') is not None:
            self.township = m.get('Township')

        return self

