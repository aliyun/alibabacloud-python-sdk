# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetVerificationInfoRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        mobile_phone: str = None,
        user_principal_name: str = None,
        verify_type: str = None,
    ):
        # The email address.
        # 
        # >  If you set `VerifyType` to `email`, you must specify this parameter.
        self.email = email
        # The mobile phone number.
        # 
        # >  If you set `VerifyType` to `sms`, you must specify this parameter.
        self.mobile_phone = mobile_phone
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name
        # The multi-factor authentication (MFA) method. Valid values:
        # 
        # *   sms: mobile phone.
        # *   email: email.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

