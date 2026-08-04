# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateOrInsertEnterpriseInfoRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        alias: str = None,
        city_json_string: Dict[str, Any] = None,
        enterprise_size: str = None,
        fax: str = None,
        name: str = None,
        pk: str = None,
        phone: str = None,
        province_json_string: Dict[str, Any] = None,
        years: str = None,
    ):
        self.address = address
        self.alias = alias
        self.city_json_string = city_json_string
        self.enterprise_size = enterprise_size
        self.fax = fax
        self.name = name
        self.pk = pk
        self.phone = phone
        self.province_json_string = province_json_string
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.city_json_string is not None:
            result['CityJsonString'] = self.city_json_string

        if self.enterprise_size is not None:
            result['EnterpriseSize'] = self.enterprise_size

        if self.fax is not None:
            result['Fax'] = self.fax

        if self.name is not None:
            result['Name'] = self.name

        if self.pk is not None:
            result['PK'] = self.pk

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.province_json_string is not None:
            result['ProvinceJsonString'] = self.province_json_string

        if self.years is not None:
            result['Years'] = self.years

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('CityJsonString') is not None:
            self.city_json_string = m.get('CityJsonString')

        if m.get('EnterpriseSize') is not None:
            self.enterprise_size = m.get('EnterpriseSize')

        if m.get('Fax') is not None:
            self.fax = m.get('Fax')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ProvinceJsonString') is not None:
            self.province_json_string = m.get('ProvinceJsonString')

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

