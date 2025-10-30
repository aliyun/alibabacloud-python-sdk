# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountsRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the database account.
        self.account_name = account_name
        # The type of the database account that you want to query. Valid values: Super, Normal, and All. Default value: Super. If you set this parameter to Super, the information about the privileged account is returned. If you set this parameter to Normal, the information about all standard accounts is returned. If you set this parameter to All, the information about all database accounts is returned.
        self.account_type = account_type
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
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

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

