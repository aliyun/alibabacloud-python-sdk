# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgAccountRequest(DaraModel):
    def __init__(
        self,
        account_attr: str = None,
        city_name: str = None,
        enterprise_name: str = None,
        first_name: str = None,
        last_name: str = None,
        login_email: str = None,
        nation_code: str = None,
        postcode: str = None,
        province_name: str = None,
    ):
        # The attribute of the account. To view the attribute of the account, use the account to log on to the Alibaba Cloud Management Console, move the pointer over the profile picture in the upper-right corner, and then click **Security Settings**.
        self.account_attr = account_attr
        # The name of the city.
        self.city_name = city_name
        # The name of the enterprise.
        self.enterprise_name = enterprise_name
        # The first name.
        self.first_name = first_name
        # The last name.
        # 
        # The last name can be up to 64 characters in length.
        self.last_name = last_name
        # The email address used to log on to the account.
        # 
        # This parameter is required.
        self.login_email = login_email
        # The country code.
        self.nation_code = nation_code
        # The zip code.
        self.postcode = postcode
        # The name of the province. This parameter is optional.
        self.province_name = province_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_attr is not None:
            result['AccountAttr'] = self.account_attr

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.login_email is not None:
            result['LoginEmail'] = self.login_email

        if self.nation_code is not None:
            result['NationCode'] = self.nation_code

        if self.postcode is not None:
            result['Postcode'] = self.postcode

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAttr') is not None:
            self.account_attr = m.get('AccountAttr')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')

        if m.get('NationCode') is not None:
            self.nation_code = m.get('NationCode')

        if m.get('Postcode') is not None:
            self.postcode = m.get('Postcode')

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        return self

