# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAccountInfoRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        name: str = None,
        telephone: str = None,
    ):
        # The email address of the account.
        self.email = email
        # The name of the account.
        self.name = name
        # The contact information of the account.
        self.telephone = telephone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        return self

