# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendVerificationCodeForEnableRDRequest(DaraModel):
    def __init__(
        self,
        secure_mobile_phone: str = None,
    ):
        # The mobile phone number that is bound to the newly created account. If you leave this parameter empty, the mobile phone number that is bound to the current account is used.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # >  Mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are not supported.
        self.secure_mobile_phone = secure_mobile_phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secure_mobile_phone is not None:
            result['SecureMobilePhone'] = self.secure_mobile_phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecureMobilePhone') is not None:
            self.secure_mobile_phone = m.get('SecureMobilePhone')

        return self

