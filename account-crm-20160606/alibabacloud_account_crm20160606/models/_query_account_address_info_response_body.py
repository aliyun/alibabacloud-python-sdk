# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryAccountAddressInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        profile_info: main_models.QueryAccountAddressInfoResponseBodyProfileInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.profile_info = profile_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.profile_info:
            self.profile_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.profile_info is not None:
            result['ProfileInfo'] = self.profile_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProfileInfo') is not None:
            temp_model = main_models.QueryAccountAddressInfoResponseBodyProfileInfo()
            self.profile_info = temp_model.from_map(m.get('ProfileInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAccountAddressInfoResponseBodyProfileInfo(DaraModel):
    def __init__(
        self,
        account_attr: str = None,
        address: str = None,
        address_2: str = None,
        address_3: str = None,
        address_4: str = None,
        address_5: str = None,
        address_6: str = None,
        city: main_models.QueryAccountAddressInfoResponseBodyProfileInfoCity = None,
        district: main_models.QueryAccountAddressInfoResponseBodyProfileInfoDistrict = None,
        email: str = None,
        havana_id: str = None,
        nationality_code: str = None,
        post_code: str = None,
        province: main_models.QueryAccountAddressInfoResponseBodyProfileInfoProvince = None,
        self_servicing_business_reg_num: str = None,
        self_servicing_identification_num: str = None,
        true_name: str = None,
        version: str = None,
    ):
        self.account_attr = account_attr
        self.address = address
        self.address_2 = address_2
        self.address_3 = address_3
        self.address_4 = address_4
        self.address_5 = address_5
        self.address_6 = address_6
        self.city = city
        self.district = district
        self.email = email
        self.havana_id = havana_id
        self.nationality_code = nationality_code
        self.post_code = post_code
        self.province = province
        self.self_servicing_business_reg_num = self_servicing_business_reg_num
        self.self_servicing_identification_num = self_servicing_identification_num
        self.true_name = true_name
        self.version = version

    def validate(self):
        if self.city:
            self.city.validate()
        if self.district:
            self.district.validate()
        if self.province:
            self.province.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_attr is not None:
            result['AccountAttr'] = self.account_attr

        if self.address is not None:
            result['Address'] = self.address

        if self.address_2 is not None:
            result['Address2'] = self.address_2

        if self.address_3 is not None:
            result['Address3'] = self.address_3

        if self.address_4 is not None:
            result['Address4'] = self.address_4

        if self.address_5 is not None:
            result['Address5'] = self.address_5

        if self.address_6 is not None:
            result['Address6'] = self.address_6

        if self.city is not None:
            result['City'] = self.city.to_map()

        if self.district is not None:
            result['District'] = self.district.to_map()

        if self.email is not None:
            result['Email'] = self.email

        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id

        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code

        if self.post_code is not None:
            result['PostCode'] = self.post_code

        if self.province is not None:
            result['Province'] = self.province.to_map()

        if self.self_servicing_business_reg_num is not None:
            result['SelfServicingBusinessRegNum'] = self.self_servicing_business_reg_num

        if self.self_servicing_identification_num is not None:
            result['SelfServicingIdentificationNum'] = self.self_servicing_identification_num

        if self.true_name is not None:
            result['TrueName'] = self.true_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAttr') is not None:
            self.account_attr = m.get('AccountAttr')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Address2') is not None:
            self.address_2 = m.get('Address2')

        if m.get('Address3') is not None:
            self.address_3 = m.get('Address3')

        if m.get('Address4') is not None:
            self.address_4 = m.get('Address4')

        if m.get('Address5') is not None:
            self.address_5 = m.get('Address5')

        if m.get('Address6') is not None:
            self.address_6 = m.get('Address6')

        if m.get('City') is not None:
            temp_model = main_models.QueryAccountAddressInfoResponseBodyProfileInfoCity()
            self.city = temp_model.from_map(m.get('City'))

        if m.get('District') is not None:
            temp_model = main_models.QueryAccountAddressInfoResponseBodyProfileInfoDistrict()
            self.district = temp_model.from_map(m.get('District'))

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')

        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')

        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')

        if m.get('Province') is not None:
            temp_model = main_models.QueryAccountAddressInfoResponseBodyProfileInfoProvince()
            self.province = temp_model.from_map(m.get('Province'))

        if m.get('SelfServicingBusinessRegNum') is not None:
            self.self_servicing_business_reg_num = m.get('SelfServicingBusinessRegNum')

        if m.get('SelfServicingIdentificationNum') is not None:
            self.self_servicing_identification_num = m.get('SelfServicingIdentificationNum')

        if m.get('TrueName') is not None:
            self.true_name = m.get('TrueName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class QueryAccountAddressInfoResponseBodyProfileInfoProvince(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class QueryAccountAddressInfoResponseBodyProfileInfoDistrict(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class QueryAccountAddressInfoResponseBodyProfileInfoCity(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

