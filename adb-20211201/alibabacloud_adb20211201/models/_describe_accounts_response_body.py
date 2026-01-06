# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsResponseBody(DaraModel):
    def __init__(
        self,
        account_list: main_models.DescribeAccountsResponseBodyAccountList = None,
        request_id: str = None,
    ):
        # The queried database accounts.
        self.account_list = account_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            self.account_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_list is not None:
            result['AccountList'] = self.account_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountList') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountList()
            self.account_list = temp_model.from_map(m.get('AccountList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountsResponseBodyAccountList(DaraModel):
    def __init__(
        self,
        dbaccount: List[main_models.DescribeAccountsResponseBodyAccountListDBAccount] = None,
    ):
        self.dbaccount = dbaccount

    def validate(self):
        if self.dbaccount:
            for v1 in self.dbaccount:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBAccount'] = []
        if self.dbaccount is not None:
            for k1 in self.dbaccount:
                result['DBAccount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbaccount = []
        if m.get('DBAccount') is not None:
            for k1 in m.get('DBAccount'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccount()
                self.dbaccount.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountListDBAccount(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        engine: str = None,
        ram_users: str = None,
    ):
        # The description of the database account.
        self.account_description = account_description
        # The name of the database account.
        self.account_name = account_name
        # The status of the database account. Valid values:
        # 
        # *   **Creating**
        # *   **Available**
        # *   **Deleting**
        self.account_status = account_status
        # The type of the database account. Valid values:
        # 
        # *   **Normal**: standard account.
        # *   **Super**: privileged account.
        self.account_type = account_type
        # The database engine of the cluster. Valid values:
        # 
        # *   **AnalyticDB**: the AnalyticDB for MySQL engine.
        # *   **Clickhouse**: the wide table engine.
        self.engine = engine
        # The ID of the Resource Access Management (RAM) user.
        self.ram_users = ram_users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.ram_users is not None:
            result['RamUsers'] = self.ram_users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('RamUsers') is not None:
            self.ram_users = m.get('RamUsers')

        return self

