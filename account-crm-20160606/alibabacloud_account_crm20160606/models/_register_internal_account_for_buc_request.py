# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterInternalAccountForBucRequest(DaraModel):
    def __init__(
        self,
        bid: str = None,
        email: str = None,
        is_email_confirmed: bool = None,
        is_mobile_confirmed: bool = None,
        is_mobile_login: bool = None,
        mobile: str = None,
        nationality_code: str = None,
        plain_password: str = None,
        preferred_language: str = None,
        account_type_code: str = None,
    ):
        # This parameter is required.
        self.bid = bid
        # This parameter is required.
        self.email = email
        self.is_email_confirmed = is_email_confirmed
        self.is_mobile_confirmed = is_mobile_confirmed
        self.is_mobile_login = is_mobile_login
        self.mobile = mobile
        self.nationality_code = nationality_code
        self.plain_password = plain_password
        self.preferred_language = preferred_language
        self.account_type_code = account_type_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.email is not None:
            result['Email'] = self.email

        if self.is_email_confirmed is not None:
            result['IsEmailConfirmed'] = self.is_email_confirmed

        if self.is_mobile_confirmed is not None:
            result['IsMobileConfirmed'] = self.is_mobile_confirmed

        if self.is_mobile_login is not None:
            result['IsMobileLogin'] = self.is_mobile_login

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code

        if self.plain_password is not None:
            result['PlainPassword'] = self.plain_password

        if self.preferred_language is not None:
            result['PreferredLanguage'] = self.preferred_language

        if self.account_type_code is not None:
            result['accountTypeCode'] = self.account_type_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IsEmailConfirmed') is not None:
            self.is_email_confirmed = m.get('IsEmailConfirmed')

        if m.get('IsMobileConfirmed') is not None:
            self.is_mobile_confirmed = m.get('IsMobileConfirmed')

        if m.get('IsMobileLogin') is not None:
            self.is_mobile_login = m.get('IsMobileLogin')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')

        if m.get('PlainPassword') is not None:
            self.plain_password = m.get('PlainPassword')

        if m.get('PreferredLanguage') is not None:
            self.preferred_language = m.get('PreferredLanguage')

        if m.get('accountTypeCode') is not None:
            self.account_type_code = m.get('accountTypeCode')

        return self

