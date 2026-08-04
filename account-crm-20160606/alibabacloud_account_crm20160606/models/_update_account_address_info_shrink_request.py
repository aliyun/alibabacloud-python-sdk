# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAccountAddressInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_2: str = None,
        city_json_string_shrink: str = None,
        district_json_string_shrink: str = None,
        pk: str = None,
        post_code: str = None,
        province_json_string_shrink: str = None,
    ):
        self.address = address
        self.address_2 = address_2
        self.city_json_string_shrink = city_json_string_shrink
        self.district_json_string_shrink = district_json_string_shrink
        self.pk = pk
        self.post_code = post_code
        self.province_json_string_shrink = province_json_string_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_2 is not None:
            result['Address2'] = self.address_2

        if self.city_json_string_shrink is not None:
            result['CityJsonString'] = self.city_json_string_shrink

        if self.district_json_string_shrink is not None:
            result['DistrictJsonString'] = self.district_json_string_shrink

        if self.pk is not None:
            result['PK'] = self.pk

        if self.post_code is not None:
            result['PostCode'] = self.post_code

        if self.province_json_string_shrink is not None:
            result['ProvinceJsonString'] = self.province_json_string_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Address2') is not None:
            self.address_2 = m.get('Address2')

        if m.get('CityJsonString') is not None:
            self.city_json_string_shrink = m.get('CityJsonString')

        if m.get('DistrictJsonString') is not None:
            self.district_json_string_shrink = m.get('DistrictJsonString')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')

        if m.get('ProvinceJsonString') is not None:
            self.province_json_string_shrink = m.get('ProvinceJsonString')

        return self

