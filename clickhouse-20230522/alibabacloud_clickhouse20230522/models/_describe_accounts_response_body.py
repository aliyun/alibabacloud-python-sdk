# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAccountsResponseBodyData = None,
        request_id: str = None,
    ):
        # The result returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountsResponseBodyData(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.DescribeAccountsResponseBodyDataAccounts] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The database accounts.
        self.accounts = accounts
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.DescribeAccountsResponseBodyDataAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccountsResponseBodyDataAccounts(DaraModel):
    def __init__(
        self,
        account: str = None,
        account_type: str = None,
        description: str = None,
        status: str = None,
    ):
        # The username of the database account.
        self.account = account
        # The type of the database account. Valid values:
        # 
        # *   **1**: standard account
        # *   **6**: privileged account
        self.account_type = account_type
        # The description.
        self.description = description
        # The state of the database account. Valid values:
        # 
        # *   **0**: The database account is being created.
        # *   **1**: The database account is in use.
        # *   **3**: The database account is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.description is not None:
            result['Description'] = self.description

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

