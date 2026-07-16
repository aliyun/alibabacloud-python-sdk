# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SimpleUser(DaraModel):
    def __init__(
        self,
        account_no: str = None,
        account_type: str = None,
        role: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # Account ID
        self.account_no = account_no
        # Account Type
        self.account_type = account_type
        # Role
        self.role = role
        # User ID
        self.user_id = user_id
        # Username
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.role is not None:
            result['Role'] = self.role

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

