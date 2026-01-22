# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.account_password = account_password
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.region_id = region_id
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password

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

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name

        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')

        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')

        return self

