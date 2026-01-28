# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveBatchTaskForUpdatingContactInfoByNewContactRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        contact_type: str = None,
        country: str = None,
        domain_name: List[str] = None,
        email: str = None,
        lang: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        transfer_out_prohibited: bool = None,
        user_client_ip: str = None,
        zh_address: str = None,
        zh_city: str = None,
        zh_province: str = None,
        zh_registrant_name: str = None,
        zh_registrant_organization: str = None,
    ):
        self.address = address
        self.city = city
        # This parameter is required.
        self.contact_type = contact_type
        self.country = country
        # This parameter is required.
        self.domain_name = domain_name
        self.email = email
        self.lang = lang
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        # This parameter is required.
        self.registrant_type = registrant_type
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.telephone = telephone
        self.transfer_out_prohibited = transfer_out_prohibited
        self.user_client_ip = user_client_ip
        self.zh_address = zh_address
        self.zh_city = zh_city
        self.zh_province = zh_province
        self.zh_registrant_name = zh_registrant_name
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

        if self.contact_type is not None:
            result['ContactType'] = self.contact_type

        if self.country is not None:
            result['Country'] = self.country

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.email is not None:
            result['Email'] = self.email

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

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited

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

        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

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

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')

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

