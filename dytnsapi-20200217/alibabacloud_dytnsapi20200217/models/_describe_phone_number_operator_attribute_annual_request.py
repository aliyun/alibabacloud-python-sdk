# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePhoneNumberOperatorAttributeAnnualRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        mask: str = None,
        number: str = None,
    ):
        self.auth_code = auth_code
        self.mask = mask
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.number is not None:
            result['Number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        return self

