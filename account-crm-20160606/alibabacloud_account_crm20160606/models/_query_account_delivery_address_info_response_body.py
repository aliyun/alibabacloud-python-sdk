# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryAccountDeliveryAddressInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryAccountDeliveryAddressInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryAccountDeliveryAddressInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccountDeliveryAddressInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        address: str = None,
        area_division: main_models.QueryAccountDeliveryAddressInfoResponseBodyDataAreaDivision = None,
        area_id: str = None,
        city_division: main_models.QueryAccountDeliveryAddressInfoResponseBodyDataCityDivision = None,
        city_id: str = None,
        contacts: str = None,
        default_address: bool = None,
        email: str = None,
        mobile: str = None,
        phone: str = None,
        pk: str = None,
        postalcode: str = None,
        provice_division: main_models.QueryAccountDeliveryAddressInfoResponseBodyDataProviceDivision = None,
        provice_id: str = None,
        town_division: main_models.QueryAccountDeliveryAddressInfoResponseBodyDataTownDivision = None,
        town_id: str = None,
    ):
        self.address = address
        self.area_division = area_division
        self.area_id = area_id
        self.city_division = city_division
        self.city_id = city_id
        self.contacts = contacts
        self.default_address = default_address
        self.email = email
        self.mobile = mobile
        self.phone = phone
        self.pk = pk
        self.postalcode = postalcode
        self.provice_division = provice_division
        self.provice_id = provice_id
        self.town_division = town_division
        self.town_id = town_id

    def validate(self):
        if self.area_division:
            self.area_division.validate()
        if self.city_division:
            self.city_division.validate()
        if self.provice_division:
            self.provice_division.validate()
        if self.town_division:
            self.town_division.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.area_division is not None:
            result['AreaDivision'] = self.area_division.to_map()

        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.city_division is not None:
            result['CityDivision'] = self.city_division.to_map()

        if self.city_id is not None:
            result['CityId'] = self.city_id

        if self.contacts is not None:
            result['Contacts'] = self.contacts

        if self.default_address is not None:
            result['DefaultAddress'] = self.default_address

        if self.email is not None:
            result['Email'] = self.email

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.postalcode is not None:
            result['Postalcode'] = self.postalcode

        if self.provice_division is not None:
            result['ProviceDivision'] = self.provice_division.to_map()

        if self.provice_id is not None:
            result['ProviceId'] = self.provice_id

        if self.town_division is not None:
            result['TownDivision'] = self.town_division.to_map()

        if self.town_id is not None:
            result['TownId'] = self.town_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AreaDivision') is not None:
            temp_model = main_models.QueryAccountDeliveryAddressInfoResponseBodyDataAreaDivision()
            self.area_division = temp_model.from_map(m.get('AreaDivision'))

        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('CityDivision') is not None:
            temp_model = main_models.QueryAccountDeliveryAddressInfoResponseBodyDataCityDivision()
            self.city_division = temp_model.from_map(m.get('CityDivision'))

        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')

        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')

        if m.get('DefaultAddress') is not None:
            self.default_address = m.get('DefaultAddress')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Postalcode') is not None:
            self.postalcode = m.get('Postalcode')

        if m.get('ProviceDivision') is not None:
            temp_model = main_models.QueryAccountDeliveryAddressInfoResponseBodyDataProviceDivision()
            self.provice_division = temp_model.from_map(m.get('ProviceDivision'))

        if m.get('ProviceId') is not None:
            self.provice_id = m.get('ProviceId')

        if m.get('TownDivision') is not None:
            temp_model = main_models.QueryAccountDeliveryAddressInfoResponseBodyDataTownDivision()
            self.town_division = temp_model.from_map(m.get('TownDivision'))

        if m.get('TownId') is not None:
            self.town_id = m.get('TownId')

        return self

class QueryAccountDeliveryAddressInfoResponseBodyDataTownDivision(DaraModel):
    def __init__(
        self,
        division_abb_name: str = None,
        division_id: int = None,
        division_level: int = None,
        division_name: str = None,
        division_tname: str = None,
        new_division_id: int = None,
        parent_id: int = None,
        pinyin: str = None,
        remark: str = None,
    ):
        self.division_abb_name = division_abb_name
        self.division_id = division_id
        self.division_level = division_level
        self.division_name = division_name
        self.division_tname = division_tname
        self.new_division_id = new_division_id
        self.parent_id = parent_id
        self.pinyin = pinyin
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_abb_name is not None:
            result['DivisionAbbName'] = self.division_abb_name

        if self.division_id is not None:
            result['DivisionId'] = self.division_id

        if self.division_level is not None:
            result['DivisionLevel'] = self.division_level

        if self.division_name is not None:
            result['DivisionName'] = self.division_name

        if self.division_tname is not None:
            result['DivisionTname'] = self.division_tname

        if self.new_division_id is not None:
            result['NewDivisionId'] = self.new_division_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DivisionAbbName') is not None:
            self.division_abb_name = m.get('DivisionAbbName')

        if m.get('DivisionId') is not None:
            self.division_id = m.get('DivisionId')

        if m.get('DivisionLevel') is not None:
            self.division_level = m.get('DivisionLevel')

        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')

        if m.get('DivisionTname') is not None:
            self.division_tname = m.get('DivisionTname')

        if m.get('NewDivisionId') is not None:
            self.new_division_id = m.get('NewDivisionId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

class QueryAccountDeliveryAddressInfoResponseBodyDataProviceDivision(DaraModel):
    def __init__(
        self,
        division_abb_name: str = None,
        division_id: int = None,
        division_level: int = None,
        division_name: str = None,
        division_tname: str = None,
        new_division_id: int = None,
        parent_id: int = None,
        pinyin: str = None,
        remark: str = None,
    ):
        self.division_abb_name = division_abb_name
        self.division_id = division_id
        self.division_level = division_level
        self.division_name = division_name
        self.division_tname = division_tname
        self.new_division_id = new_division_id
        self.parent_id = parent_id
        self.pinyin = pinyin
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_abb_name is not None:
            result['DivisionAbbName'] = self.division_abb_name

        if self.division_id is not None:
            result['DivisionId'] = self.division_id

        if self.division_level is not None:
            result['DivisionLevel'] = self.division_level

        if self.division_name is not None:
            result['DivisionName'] = self.division_name

        if self.division_tname is not None:
            result['DivisionTname'] = self.division_tname

        if self.new_division_id is not None:
            result['NewDivisionId'] = self.new_division_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DivisionAbbName') is not None:
            self.division_abb_name = m.get('DivisionAbbName')

        if m.get('DivisionId') is not None:
            self.division_id = m.get('DivisionId')

        if m.get('DivisionLevel') is not None:
            self.division_level = m.get('DivisionLevel')

        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')

        if m.get('DivisionTname') is not None:
            self.division_tname = m.get('DivisionTname')

        if m.get('NewDivisionId') is not None:
            self.new_division_id = m.get('NewDivisionId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

class QueryAccountDeliveryAddressInfoResponseBodyDataCityDivision(DaraModel):
    def __init__(
        self,
        division_abb_name: str = None,
        division_id: int = None,
        division_level: int = None,
        division_name: str = None,
        division_tname: str = None,
        new_division_id: int = None,
        parent_id: int = None,
        pinyin: str = None,
        remark: str = None,
    ):
        self.division_abb_name = division_abb_name
        self.division_id = division_id
        self.division_level = division_level
        self.division_name = division_name
        self.division_tname = division_tname
        self.new_division_id = new_division_id
        self.parent_id = parent_id
        self.pinyin = pinyin
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_abb_name is not None:
            result['DivisionAbbName'] = self.division_abb_name

        if self.division_id is not None:
            result['DivisionId'] = self.division_id

        if self.division_level is not None:
            result['DivisionLevel'] = self.division_level

        if self.division_name is not None:
            result['DivisionName'] = self.division_name

        if self.division_tname is not None:
            result['DivisionTname'] = self.division_tname

        if self.new_division_id is not None:
            result['NewDivisionId'] = self.new_division_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DivisionAbbName') is not None:
            self.division_abb_name = m.get('DivisionAbbName')

        if m.get('DivisionId') is not None:
            self.division_id = m.get('DivisionId')

        if m.get('DivisionLevel') is not None:
            self.division_level = m.get('DivisionLevel')

        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')

        if m.get('DivisionTname') is not None:
            self.division_tname = m.get('DivisionTname')

        if m.get('NewDivisionId') is not None:
            self.new_division_id = m.get('NewDivisionId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

class QueryAccountDeliveryAddressInfoResponseBodyDataAreaDivision(DaraModel):
    def __init__(
        self,
        division_abb_name: str = None,
        division_id: int = None,
        division_level: int = None,
        division_name: str = None,
        division_tname: str = None,
        new_division_id: int = None,
        parent_id: int = None,
        pinyin: str = None,
        remark: str = None,
    ):
        self.division_abb_name = division_abb_name
        self.division_id = division_id
        self.division_level = division_level
        self.division_name = division_name
        self.division_tname = division_tname
        self.new_division_id = new_division_id
        self.parent_id = parent_id
        self.pinyin = pinyin
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_abb_name is not None:
            result['DivisionAbbName'] = self.division_abb_name

        if self.division_id is not None:
            result['DivisionId'] = self.division_id

        if self.division_level is not None:
            result['DivisionLevel'] = self.division_level

        if self.division_name is not None:
            result['DivisionName'] = self.division_name

        if self.division_tname is not None:
            result['DivisionTname'] = self.division_tname

        if self.new_division_id is not None:
            result['NewDivisionId'] = self.new_division_id

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DivisionAbbName') is not None:
            self.division_abb_name = m.get('DivisionAbbName')

        if m.get('DivisionId') is not None:
            self.division_id = m.get('DivisionId')

        if m.get('DivisionLevel') is not None:
            self.division_level = m.get('DivisionLevel')

        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')

        if m.get('DivisionTname') is not None:
            self.division_tname = m.get('DivisionTname')

        if m.get('NewDivisionId') is not None:
            self.new_division_id = m.get('NewDivisionId')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

