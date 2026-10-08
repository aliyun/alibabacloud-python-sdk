# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryContactInfoResponseBody(DaraModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        create_date: str = None,
        email: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        request_id: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        zh_address: str = None,
        zh_city: str = None,
        zh_province: str = None,
        zh_registrant_name: str = None,
        zh_registrant_organization: str = None,
    ):
        # Mailing address (English).
        self.address = address
        # City (English).
        self.city = city
        # Country code. For example, **CN** represents China and **US** represents the United States.
        self.country = country
        # Domain registration date.
        self.create_date = create_date
        # Mailbox.
        self.email = email
        # Postal code.
        self.postal_code = postal_code
        # Province (English).
        self.province = province
        # Contact name (English).
        self.registrant_name = registrant_name
        # Registrant name (English).
        self.registrant_organization = registrant_organization
        # Unique request access token.
        self.request_id = request_id
        # The country code for the telephone number. For example, the country code for China is **86**.
        self.tel_area = tel_area
        # Telephone extension number.
        self.tel_ext = tel_ext
        # Telephone number.
        self.telephone = telephone
        # Mailing address (in Chinese).
        self.zh_address = zh_address
        # City (Chinese).
        self.zh_city = zh_city
        # Province (Chinese).
        self.zh_province = zh_province
        # Contact name (Chinese).
        self.zh_registrant_name = zh_registrant_name
        # Registrant name (Chinese).
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

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.email is not None:
            result['Email'] = self.email

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.province is not None:
            result['Province'] = self.province

        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name

        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.telephone is not None:
            result['Telephone'] = self.telephone

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

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')

        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

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

