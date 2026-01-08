# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPreValidatePhoneIdRequest(DaraModel):
    def __init__(
        self,
        phone_number: str = None,
        verify_code: str = None,
    ):
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The verification code provided when you purchased the pre-registered phone number.
        # 
        # This parameter is required.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        return self

