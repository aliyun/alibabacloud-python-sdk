# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCompanyResponseBody(DaraModel):
    def __init__(
        self,
        city: str = None,
        company_address: str = None,
        company_code: str = None,
        company_email: str = None,
        company_id: int = None,
        company_name: str = None,
        company_phone: str = None,
        company_type: int = None,
        country_code: str = None,
        department: str = None,
        lang: str = None,
        post_code: str = None,
        province: str = None,
        request_id: str = None,
    ):
        # The city.
        self.city = city
        # The address of the company.
        self.company_address = company_address
        # The company code.
        self.company_code = company_code
        # The email address of the company.
        self.company_email = company_email
        # The company ID.
        self.company_id = company_id
        # The name of the company or organization.
        self.company_name = company_name
        # The phone number of the company.
        self.company_phone = company_phone
        # The company type.
        self.company_type = company_type
        # The country code.
        self.country_code = country_code
        # The department.
        self.department = department
        # The language.
        self.lang = lang
        # The postal code.
        self.post_code = post_code
        # The province.
        self.province = province
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.company_address is not None:
            result['CompanyAddress'] = self.company_address

        if self.company_code is not None:
            result['CompanyCode'] = self.company_code

        if self.company_email is not None:
            result['CompanyEmail'] = self.company_email

        if self.company_id is not None:
            result['CompanyId'] = self.company_id

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.company_phone is not None:
            result['CompanyPhone'] = self.company_phone

        if self.company_type is not None:
            result['CompanyType'] = self.company_type

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.department is not None:
            result['Department'] = self.department

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.post_code is not None:
            result['PostCode'] = self.post_code

        if self.province is not None:
            result['Province'] = self.province

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CompanyAddress') is not None:
            self.company_address = m.get('CompanyAddress')

        if m.get('CompanyCode') is not None:
            self.company_code = m.get('CompanyCode')

        if m.get('CompanyEmail') is not None:
            self.company_email = m.get('CompanyEmail')

        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('CompanyPhone') is not None:
            self.company_phone = m.get('CompanyPhone')

        if m.get('CompanyType') is not None:
            self.company_type = m.get('CompanyType')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

