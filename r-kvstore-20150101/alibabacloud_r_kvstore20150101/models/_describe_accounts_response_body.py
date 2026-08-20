# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsResponseBody(DaraModel):
    def __init__(
        self,
        accounts: main_models.DescribeAccountsResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.accounts = accounts
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccountsResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        account: List[main_models.DescribeAccountsResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for v1 in self.account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Account'] = []
        if self.account is not None:
            for k1 in self.account:
                result['Account'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k1 in m.get('Account'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountsAccount(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        database_privileges: main_models.DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges = None,
        instance_id: str = None,
        parameters: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_status = account_status
        self.account_type = account_type
        self.database_privileges = database_privileges
        self.instance_id = instance_id
        self.parameters = parameters

    def validate(self):
        if self.database_privileges:
            self.database_privileges.validate()

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

        if self.database_privileges is not None:
            result['DatabasePrivileges'] = self.database_privileges.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

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

        if m.get('DatabasePrivileges') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges()
            self.database_privileges = temp_model.from_map(m.get('DatabasePrivileges'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

class DescribeAccountsResponseBodyAccountsAccountDatabasePrivileges(DaraModel):
    def __init__(
        self,
        database_privilege: List[main_models.DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege] = None,
    ):
        self.database_privilege = database_privilege

    def validate(self):
        if self.database_privilege:
            for v1 in self.database_privilege:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabasePrivilege'] = []
        if self.database_privilege is not None:
            for k1 in self.database_privilege:
                result['DatabasePrivilege'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_privilege = []
        if m.get('DatabasePrivilege') is not None:
            for k1 in m.get('DatabasePrivilege'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege()
                self.database_privilege.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountsAccountDatabasePrivilegesDatabasePrivilege(DaraModel):
    def __init__(
        self,
        account_privilege: str = None,
    ):
        self.account_privilege = account_privilege

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        return self

