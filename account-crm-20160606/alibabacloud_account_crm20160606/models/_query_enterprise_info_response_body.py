# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryEnterpriseInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        profile_info: main_models.QueryEnterpriseInfoResponseBodyProfileInfo = None,
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
            temp_model = main_models.QueryEnterpriseInfoResponseBodyProfileInfo()
            self.profile_info = temp_model.from_map(m.get('ProfileInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryEnterpriseInfoResponseBodyProfileInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        aliyun_pk: str = None,
        audit_status: str = None,
        business_license_img_src: str = None,
        business_license_number: str = None,
        business_license_type: str = None,
        certified_from: str = None,
        certified_time: str = None,
        city: main_models.QueryEnterpriseInfoResponseBodyProfileInfoCity = None,
        create_time: str = None,
        detail_address: str = None,
        einterprise_size: str = None,
        enterprise_entity: str = None,
        entity_idnumber: str = None,
        extend: str = None,
        fax: str = None,
        name: str = None,
        phone: str = None,
        postal_code: str = None,
        profile: str = None,
        province: main_models.QueryEnterpriseInfoResponseBodyProfileInfoProvince = None,
        update_time: str = None,
        years: str = None,
    ):
        self.alias = alias
        self.aliyun_pk = aliyun_pk
        self.audit_status = audit_status
        self.business_license_img_src = business_license_img_src
        self.business_license_number = business_license_number
        self.business_license_type = business_license_type
        self.certified_from = certified_from
        self.certified_time = certified_time
        self.city = city
        self.create_time = create_time
        self.detail_address = detail_address
        self.einterprise_size = einterprise_size
        self.enterprise_entity = enterprise_entity
        self.entity_idnumber = entity_idnumber
        self.extend = extend
        self.fax = fax
        self.name = name
        self.phone = phone
        self.postal_code = postal_code
        self.profile = profile
        self.province = province
        self.update_time = update_time
        self.years = years

    def validate(self):
        if self.city:
            self.city.validate()
        if self.province:
            self.province.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.aliyun_pk is not None:
            result['AliyunPK'] = self.aliyun_pk

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.business_license_img_src is not None:
            result['BusinessLicenseImgSrc'] = self.business_license_img_src

        if self.business_license_number is not None:
            result['BusinessLicenseNumber'] = self.business_license_number

        if self.business_license_type is not None:
            result['BusinessLicenseType'] = self.business_license_type

        if self.certified_from is not None:
            result['CertifiedFrom'] = self.certified_from

        if self.certified_time is not None:
            result['CertifiedTime'] = self.certified_time

        if self.city is not None:
            result['City'] = self.city.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.detail_address is not None:
            result['DetailAddress'] = self.detail_address

        if self.einterprise_size is not None:
            result['EInterpriseSize'] = self.einterprise_size

        if self.enterprise_entity is not None:
            result['EnterpriseEntity'] = self.enterprise_entity

        if self.entity_idnumber is not None:
            result['EntityIDNumber'] = self.entity_idnumber

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.fax is not None:
            result['Fax'] = self.fax

        if self.name is not None:
            result['Name'] = self.name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.province is not None:
            result['Province'] = self.province.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.years is not None:
            result['Years'] = self.years

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AliyunPK') is not None:
            self.aliyun_pk = m.get('AliyunPK')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('BusinessLicenseImgSrc') is not None:
            self.business_license_img_src = m.get('BusinessLicenseImgSrc')

        if m.get('BusinessLicenseNumber') is not None:
            self.business_license_number = m.get('BusinessLicenseNumber')

        if m.get('BusinessLicenseType') is not None:
            self.business_license_type = m.get('BusinessLicenseType')

        if m.get('CertifiedFrom') is not None:
            self.certified_from = m.get('CertifiedFrom')

        if m.get('CertifiedTime') is not None:
            self.certified_time = m.get('CertifiedTime')

        if m.get('City') is not None:
            temp_model = main_models.QueryEnterpriseInfoResponseBodyProfileInfoCity()
            self.city = temp_model.from_map(m.get('City'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DetailAddress') is not None:
            self.detail_address = m.get('DetailAddress')

        if m.get('EInterpriseSize') is not None:
            self.einterprise_size = m.get('EInterpriseSize')

        if m.get('EnterpriseEntity') is not None:
            self.enterprise_entity = m.get('EnterpriseEntity')

        if m.get('EntityIDNumber') is not None:
            self.entity_idnumber = m.get('EntityIDNumber')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Fax') is not None:
            self.fax = m.get('Fax')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Province') is not None:
            temp_model = main_models.QueryEnterpriseInfoResponseBodyProfileInfoProvince()
            self.province = temp_model.from_map(m.get('Province'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

class QueryEnterpriseInfoResponseBodyProfileInfoProvince(DaraModel):
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

class QueryEnterpriseInfoResponseBodyProfileInfoCity(DaraModel):
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

