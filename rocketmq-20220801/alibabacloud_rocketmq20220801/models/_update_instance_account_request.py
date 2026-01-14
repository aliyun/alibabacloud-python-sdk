# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceAccountRequest(DaraModel):
    def __init__(
        self,
        account_status: str = None,
        password: str = None,
    ):
        # The status of the account.
        # 
        # Valid values:
        # 
        # *   DISABLE
        # *   ENABLE
        self.account_status = account_status
        # The password of the account.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_status is not None:
            result['accountStatus'] = self.account_status

        if self.password is not None:
            result['password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')

        if m.get('password') is not None:
            self.password = m.get('password')

        return self

