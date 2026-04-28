# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Address(DaraModel):
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
        # The country or region.
        self.country = country
        # The district.
        self.district = district
        # The province.
        self.province = province
        # The street.
        self.township = township

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['city'] = self.city

        if self.country is not None:
            result['country'] = self.country

        if self.district is not None:
            result['district'] = self.district

        if self.province is not None:
            result['province'] = self.province

        if self.township is not None:
            result['township'] = self.township

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('country') is not None:
            self.country = m.get('country')

        if m.get('district') is not None:
            self.district = m.get('district')

        if m.get('province') is not None:
            self.province = m.get('province')

        if m.get('township') is not None:
            self.township = m.get('township')

        return self

