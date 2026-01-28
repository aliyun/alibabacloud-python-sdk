# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryRegistrantProfilesResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        registrant_profiles: main_models.QueryRegistrantProfilesResponseBodyRegistrantProfiles = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The page number returned.
        self.current_page_num = current_page_num
        # Indicates whether the current page is followed by a page. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.next_page = next_page
        # The number of entries returned on each page. Default value: **0**. Maximum value: **5000**.
        self.page_size = page_size
        # Indicates whether the current page is preceded by a page. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.pre_page = pre_page
        # The list of registrant profiles.
        self.registrant_profiles = registrant_profiles
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        # 
        # >  This parameter indicates the total number of queried registrant profiles. If multiple registrant profiles are queried, the information about these profiles is returned in sequence by profile.
        self.total_item_num = total_item_num
        # The total number of returned pages.
        self.total_page_num = total_page_num

    def validate(self):
        if self.registrant_profiles:
            self.registrant_profiles.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.registrant_profiles is not None:
            result['RegistrantProfiles'] = self.registrant_profiles.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RegistrantProfiles') is not None:
            temp_model = main_models.QueryRegistrantProfilesResponseBodyRegistrantProfiles()
            self.registrant_profiles = temp_model.from_map(m.get('RegistrantProfiles'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryRegistrantProfilesResponseBodyRegistrantProfiles(DaraModel):
    def __init__(
        self,
        registrant_profile: List[main_models.QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile] = None,
    ):
        self.registrant_profile = registrant_profile

    def validate(self):
        if self.registrant_profile:
            for v1 in self.registrant_profile:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegistrantProfile'] = []
        if self.registrant_profile is not None:
            for k1 in self.registrant_profile:
                result['RegistrantProfile'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.registrant_profile = []
        if m.get('RegistrantProfile') is not None:
            for k1 in m.get('RegistrantProfile'):
                temp_model = main_models.QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile()
                self.registrant_profile.append(temp_model.from_map(k1))

        return self

class QueryRegistrantProfilesResponseBodyRegistrantProfilesRegistrantProfile(DaraModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        create_time: str = None,
        credential_no: str = None,
        credential_type: str = None,
        default_registrant_profile: bool = None,
        email: str = None,
        email_verification_status: int = None,
        params: str = None,
        postal_code: str = None,
        province: str = None,
        real_name_status: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_profile_type: str = None,
        registrant_type: str = None,
        remark: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        update_time: str = None,
        zh_address: str = None,
        zh_city: str = None,
        zh_province: str = None,
        zh_registrant_name: str = None,
        zh_registrant_organization: str = None,
    ):
        # The address of the domain name registrant.
        self.address = address
        # The city where the domain name registrant is located, in English.
        self.city = city
        # The code of the country or region where the domain name registrant is located, such as **CN** or **US**.
        self.country = country
        # The time when the registrant profile was created.
        self.create_time = create_time
        # The certificate number.
        self.credential_no = credential_no
        # The certificate type.
        self.credential_type = credential_type
        # Indicates whether the template is the default template. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # Default value: **false**.
        self.default_registrant_profile = default_registrant_profile
        # The email address of the domain name registrant.
        self.email = email
        # The status of the verification for the email address. Valid values:
        # 
        # *   **0**: not verified
        # *   **1**: verified
        self.email_verification_status = email_verification_status
        self.params = params
        # The postal code of the region where the domain name registrant is located.
        self.postal_code = postal_code
        # The province where the domain name registrant is located.
        self.province = province
        # The state of real-name verification for the domain name registrant. Valid values:
        # 
        # *   **FAILED**: Real-name verification for the domain name fails.
        # *   **SUCCEED**: Real-name verification for the domain name is successful.
        # *   **NONAUDIT**: Real-name verification for the domain name is not performed.
        # *   **AUDITING**: Real-name verification for the domain name is in progress.
        self.real_name_status = real_name_status
        # The name of the domain name contact.
        self.registrant_name = registrant_name
        # The name of the domain name registrant.
        self.registrant_organization = registrant_organization
        # The ID of the registrant profile.
        self.registrant_profile_id = registrant_profile_id
        # The type of the registrant profile. Valid values:
        # 
        # *   **common**: common profile.
        # *   **cnnic**: CNNIC profile.
        # 
        # >  Only the Alibaba Cloud international site (alibabacloud.com) supports CNNIC profiles. To register domain names provided by CNNIC such as the .cn and . domain names on the Alibaba Cloud international site, you must use a CNNIC profile. To register other domain names, use a common profile.
        self.registrant_profile_type = registrant_profile_type
        # The type of the domain name registrant. Valid values:
        # 
        # *   **1**: individual.
        # *   **2**: enterprise.
        # 
        # Default value: **1**.
        self.registrant_type = registrant_type
        # The remarks.
        self.remark = remark
        # The international dialing code of the country or region where the domain name contact is located. For example, the international dialing code of China is **86**.
        self.tel_area = tel_area
        # The extension of the phone number.
        self.tel_ext = tel_ext
        # The phone number.
        self.telephone = telephone
        # The time when the registrant profile was updated.
        self.update_time = update_time
        # The address of the domain name registrant, in Chinese.
        self.zh_address = zh_address
        # The city where the domain name registrant is located, in Chinese.
        self.zh_city = zh_city
        # The province where the domain name registrant is located, in Chinese.
        self.zh_province = zh_province
        # The Chinese name of the domain name contact.
        self.zh_registrant_name = zh_registrant_name
        # The Chinese name of the domain name registrant.
        self.zh_registrant_organization = zh_registrant_organization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.default_registrant_profile is not None:
            result['DefaultRegistrantProfile'] = self.default_registrant_profile

        if self.email is not None:
            result['Email'] = self.email

        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status

        if self.params is not None:
            result['Params'] = self.params

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.province is not None:
            result['Province'] = self.province

        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status

        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name

        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.registrant_profile_type is not None:
            result['RegistrantProfileType'] = self.registrant_profile_type

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.zh_address is not None:
            result['ZhAddress'] = self.zh_address

        if self.zh_city is not None:
            result['ZhCity'] = self.zh_city

        if self.zh_province is not None:
            result['ZhProvince'] = self.zh_province

        if self.zh_registrant_name is not None:
            result['ZhRegistrantName'] = self.zh_registrant_name

        if self.zh_registrant_organization is not None:
            result['ZhRegistrantOrganization'] = self.zh_registrant_organization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('DefaultRegistrantProfile') is not None:
            self.default_registrant_profile = m.get('DefaultRegistrantProfile')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')

        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')

        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('RegistrantProfileType') is not None:
            self.registrant_profile_type = m.get('RegistrantProfileType')

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('ZhAddress') is not None:
            self.zh_address = m.get('ZhAddress')

        if m.get('ZhCity') is not None:
            self.zh_city = m.get('ZhCity')

        if m.get('ZhProvince') is not None:
            self.zh_province = m.get('ZhProvince')

        if m.get('ZhRegistrantName') is not None:
            self.zh_registrant_name = m.get('ZhRegistrantName')

        if m.get('ZhRegistrantOrganization') is not None:
            self.zh_registrant_organization = m.get('ZhRegistrantOrganization')

        return self

