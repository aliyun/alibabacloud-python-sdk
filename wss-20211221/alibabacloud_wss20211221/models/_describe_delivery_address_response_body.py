# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeDeliveryAddressResponseBody(DaraModel):
    def __init__(
        self,
        addresses: List[main_models.DescribeDeliveryAddressResponseBodyAddresses] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.addresses = addresses
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k1 in m.get('Addresses'):
                temp_model = main_models.DescribeDeliveryAddressResponseBodyAddresses()
                self.addresses.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDeliveryAddressResponseBodyAddresses(DaraModel):
    def __init__(
        self,
        area: main_models.DescribeDeliveryAddressResponseBodyAddressesArea = None,
        city: main_models.DescribeDeliveryAddressResponseBodyAddressesCity = None,
        contacts: str = None,
        default_address: bool = None,
        detail: str = None,
        mobile: str = None,
        postal_code: str = None,
        province: main_models.DescribeDeliveryAddressResponseBodyAddressesProvince = None,
        town: main_models.DescribeDeliveryAddressResponseBodyAddressesTown = None,
    ):
        self.area = area
        self.city = city
        self.contacts = contacts
        self.default_address = default_address
        self.detail = detail
        self.mobile = mobile
        self.postal_code = postal_code
        self.province = province
        self.town = town

    def validate(self):
        if self.area:
            self.area.validate()
        if self.city:
            self.city.validate()
        if self.province:
            self.province.validate()
        if self.town:
            self.town.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area.to_map()

        if self.city is not None:
            result['City'] = self.city.to_map()

        if self.contacts is not None:
            result['Contacts'] = self.contacts

        if self.default_address is not None:
            result['DefaultAddress'] = self.default_address

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.province is not None:
            result['Province'] = self.province.to_map()

        if self.town is not None:
            result['Town'] = self.town.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            temp_model = main_models.DescribeDeliveryAddressResponseBodyAddressesArea()
            self.area = temp_model.from_map(m.get('Area'))

        if m.get('City') is not None:
            temp_model = main_models.DescribeDeliveryAddressResponseBodyAddressesCity()
            self.city = temp_model.from_map(m.get('City'))

        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')

        if m.get('DefaultAddress') is not None:
            self.default_address = m.get('DefaultAddress')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Province') is not None:
            temp_model = main_models.DescribeDeliveryAddressResponseBodyAddressesProvince()
            self.province = temp_model.from_map(m.get('Province'))

        if m.get('Town') is not None:
            temp_model = main_models.DescribeDeliveryAddressResponseBodyAddressesTown()
            self.town = temp_model.from_map(m.get('Town'))

        return self

class DescribeDeliveryAddressResponseBodyAddressesTown(DaraModel):
    def __init__(
        self,
        town_id: int = None,
        town_name: str = None,
    ):
        self.town_id = town_id
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.town_id is not None:
            result['TownId'] = self.town_id

        if self.town_name is not None:
            result['TownName'] = self.town_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TownId') is not None:
            self.town_id = m.get('TownId')

        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')

        return self

class DescribeDeliveryAddressResponseBodyAddressesProvince(DaraModel):
    def __init__(
        self,
        province_id: int = None,
        province_name: str = None,
    ):
        self.province_id = province_id
        self.province_name = province_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        return self

class DescribeDeliveryAddressResponseBodyAddressesCity(DaraModel):
    def __init__(
        self,
        city_id: int = None,
        city_name: str = None,
    ):
        self.city_id = city_id
        self.city_name = city_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_id is not None:
            result['CityId'] = self.city_id

        if self.city_name is not None:
            result['CityName'] = self.city_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        return self

class DescribeDeliveryAddressResponseBodyAddressesArea(DaraModel):
    def __init__(
        self,
        area_id: int = None,
        area_name: str = None,
    ):
        self.area_id = area_id
        self.area_name = area_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.area_name is not None:
            result['AreaName'] = self.area_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')

        return self

