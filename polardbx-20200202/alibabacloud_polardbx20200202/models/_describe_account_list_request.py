# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountListRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        # The name of the account. Specify this parameter to query a specific account.
        self.account_name = account_name
        # The type of the account. Specify this parameter to query accounts of a specific type. If you set this parameter to null, all accounts are returned.
        # 
        # - Before three-role mode is enabled: 0 indicates a standard account, and 1 indicates a privileged user account.
        # - After three-role mode is enabled: 0 indicates a standard account, 2 indicates a system administrator account, 3 indicates a security administrator account, and 4 indicates an audit administrator account.
        self.account_type = account_type
        # The name of the instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

