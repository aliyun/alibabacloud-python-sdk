# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsResponseBody(DaraModel):
    def __init__(
        self,
        accounts: main_models.DescribeAccountsResponseBodyAccounts = None,
        request_id: str = None,
    ):
        # The queried database accounts.
        self.accounts = accounts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountsResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        dbinstance_account: List[main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccount] = None,
    ):
        self.dbinstance_account = dbinstance_account

    def validate(self):
        if self.dbinstance_account:
            for v1 in self.dbinstance_account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceAccount'] = []
        if self.dbinstance_account is not None:
            for k1 in self.dbinstance_account:
                result['DBInstanceAccount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_account = []
        if m.get('DBInstanceAccount') is not None:
            for k1 in m.get('DBInstanceAccount'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountsDBInstanceAccount()
                self.dbinstance_account.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountsDBInstanceAccount(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        dbinstance_id: str = None,
    ):
        # The description of the account.
        self.account_description = account_description
        # The name of the account.
        self.account_name = account_name
        # The state of the account.
        # 
        # *   **0**: The account is being created.
        # *   **1**: The account is in use.
        # *   **3**: The account is being deleted.
        self.account_status = account_status
        # The type of the database account. Valid values: Super and Normal. Super indicates a privileged account and Normal indicates a standard account.
        self.account_type = account_type
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id

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

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

