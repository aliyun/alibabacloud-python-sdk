# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveRegistrantProfileRealNameVerificationRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        email: str = None,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        lang: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_profile_id: int = None,
        registrant_profile_type: str = None,
        registrant_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        user_client_ip: str = None,
        zh_address: str = None,
        zh_city: str = None,
        zh_province: str = None,
        zh_registrant_name: str = None,
        zh_registrant_organization: str = None,
    ):
        # Detailed address (in English).  
        # 
        # > This parameter is available and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.address = address
        # City (in English).  
        # 
        # > This parameter is active and required only when the **RegistrantProfileId** parameter is not provided. If this parameter is not provided, domain name registration will fail.
        self.city = city
        # Country code, such as **CN**.
        # 
        # > This parameter is active and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.country = country
        # Email address.  
        # 
        # > This parameter is available and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.email = email
        # Base64-encoded image of the identity verification document. Image requirements:  
        # - Format must be **jpg** or **bmp**.  
        # - Original image size must be between **55 KB and 1 MB**.
        self.identity_credential = identity_credential
        # Certificate number for identity verification.
        self.identity_credential_no = identity_credential_no
        # Type of certificate used for identity verification. Valid values:  
        # - **SFZ**: Identity card.  
        # - **HZ**: Passport.  
        # - **YYZZ**: Business license.  
        # - **ORG**: Organization code certificate.  
        # - **XYDM**: Unified Social Credit Code certificate.  
        # - **TXZ**: Mainland Travel Permits for Hong Kong and Macao Residents.  
        # 
        # > For more certificate types, see [Supported Certificate Types for Identity Verification](https://help.aliyun.com/document_detail/72209.html).
        self.identity_credential_type = identity_credential_type
        # Language of the error message returned by the API. Valid values:  
        # - **zh**: Chinese  
        # - **en**: English  
        # 
        # Default value: **en**.
        self.lang = lang
        # Postal code.  
        # 
        # > This parameter is available and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.postal_code = postal_code
        # Province (in English).  
        # 
        # > This parameter is active and required only when the **RegistrantProfileId** parameter is not provided. If this parameter is not provided, domain name registration will fail.
        self.province = province
        # Domain name contact (in English).  
        # 
        # > This parameter is active and required only when the **RegistrantProfileId** parameter is not provided. If this parameter is not provided, domain name registration will fail.
        self.registrant_name = registrant_name
        # Registrant name (in English).
        # 
        # > This parameter is active and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.registrant_organization = registrant_organization
        # ID of the registrant profile template to be saved.  
        # 
        # The system automatically generates this ID after a registrant profile is successfully created. You can invoke the [QueryRegistrantProfiles](https://help.aliyun.com/document_detail/67701.html) API to query the registrant profile ID.
        self.registrant_profile_id = registrant_profile_id
        # Templatetype. Valid values:  
        # - **common**: General template.  
        # - **cnnic**: CNNIC template.  
        # 
        # > The CNNIC template is supported only on the Alibaba Cloud international site (alibabacloud.com). Domains under the CNNIC registry, such as ".cn" and ".中国", registered on the Alibaba Cloud international site must use the CNNIC template. Other domains must use the general template.
        self.registrant_profile_type = registrant_profile_type
        # Type of the registrant. Valid values:  
        # - **1**: Individual.  
        # - **2**: Enterprise or organization.  
        # 
        # > This parameter is available and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.registrant_type = registrant_type
        # Telephone country code.
        # 
        # > For example, the telephone country code for China is **86**.
        self.tel_area = tel_area
        # Extension number.
        # 
        # > This parameter is active and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.tel_ext = tel_ext
        # Telephone number.  
        # 
        # > This parameter is available and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.telephone = telephone
        # User IP address. You can set it to **127.0.0.1**.
        self.user_client_ip = user_client_ip
        # Full address (in Chinese).
        # 
        # > This parameter applies only to the China site (aliyun.com). It is active and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.zh_address = zh_address
        # City (in Chinese).  
        # 
        # > This parameter applies only to the China site (aliyun.com). It is active and required only when the **RegistrantProfileId** parameter is not provided. If this parameter is not provided, domain name registration will fail.
        self.zh_city = zh_city
        # Province (in Chinese).  
        # 
        # > This parameter applies only to the China site (aliyun.com). It is available and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
        self.zh_province = zh_province
        # Domain name contact (in Chinese).  
        # 
        # > This parameter applies only to the China site (aliyun.com). It is active and required only when the **RegistrantProfileId** parameter is not provided. If this parameter is not provided, domain name registration will fail.
        self.zh_registrant_name = zh_registrant_name
        # Registrant name (in Chinese).
        # 
        # > This parameter applies only to the China site (aliyun.com). It is active and required only when the **RegistrantProfileId** parameter is not provided. Failure to provide it will cause domain registration to fail.
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

        if self.email is not None:
            result['Email'] = self.email

        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential

        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no

        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.province is not None:
            result['Province'] = self.province

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

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

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

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')

        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')

        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

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

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

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

