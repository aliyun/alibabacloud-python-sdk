# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dbinstance_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The name of the account.
        # 
        # This parameter is required.
        self.account_password = account_password
        # Before you call this operation, make sure that the following requirements are met:
        # 
        # *   The instance is in the running state.
        # *   The instance is not locked.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

