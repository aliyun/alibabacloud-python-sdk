# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Developer(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        codeup_account_id: str = None,
        email: str = None,
        enterprise_id: int = None,
        name: str = None,
        phone: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.codeup_account_id = codeup_account_id
        # This parameter is required.
        self.email = email
        self.enterprise_id = enterprise_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.phone = phone
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.codeup_account_id is not None:
            result['codeupAccountId'] = self.codeup_account_id

        if self.email is not None:
            result['email'] = self.email

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('codeupAccountId') is not None:
            self.codeup_account_id = m.get('codeupAccountId')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

