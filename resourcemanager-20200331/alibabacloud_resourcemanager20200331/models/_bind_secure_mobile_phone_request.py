# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindSecureMobilePhoneRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        secure_mobile_phone: str = None,
        verification_code: str = None,
    ):
        # The member ID.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The secure phone number.
        # 
        # The phone number must be the same as the one that you specified when you called [SendVerificationCodeForBindSecureMobilePhone](https://help.aliyun.com/document_detail/372556.html) to authenticate and obtain the verification code.
        # 
        # Format: <Country code>-<Phone number>.
        # 
        # <props="china">
        # > Only the Chinese mainland phone numbers in the `86-<Phone number>` format are supported.
        # 
        # 
        # <props="intl">
        # > The Chinese mainland phone numbers in the `86-<Phone number>` format are not supported.
        # 
        # This parameter is required.
        self.secure_mobile_phone = secure_mobile_phone
        # The verification code.
        # 
        # You can call [SendVerificationCodeForBindSecureMobilePhone](https://help.aliyun.com/document_detail/372556.html) to obtain the verification code.
        # 
        # This parameter is required.
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone

        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        return self

