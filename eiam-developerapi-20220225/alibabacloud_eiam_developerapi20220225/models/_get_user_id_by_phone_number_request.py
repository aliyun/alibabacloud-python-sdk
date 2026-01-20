# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserIdByPhoneNumberRequest(DaraModel):
    def __init__(
        self,
        phone_number: str = None,
    ):
        # The mobile number of the user who owns the account.
        # 
        # This parameter is required.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')

        return self

