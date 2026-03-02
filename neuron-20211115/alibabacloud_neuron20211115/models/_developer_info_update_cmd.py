# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeveloperInfoUpdateCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        email: str = None,
        enterprise_id: int = None,
        name: str = None,
        phone: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.email = email
        self.enterprise_id = enterprise_id
        self.name = name
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.email is not None:
            result['email'] = self.email

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

