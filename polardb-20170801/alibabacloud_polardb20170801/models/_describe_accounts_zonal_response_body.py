# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsZonalResponseBody(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.DescribeAccountsZonalResponseBodyAccounts] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
    ):
        self.accounts = accounts
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.DescribeAccountsZonalResponseBodyAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountsZonalResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_lock_state: str = None,
        account_name: str = None,
        account_password_valid_time: str = None,
        account_status: str = None,
        account_type: str = None,
        database_privileges: List[main_models.DescribeAccountsZonalResponseBodyAccountsDatabasePrivileges] = None,
    ):
        self.account_description = account_description
        self.account_lock_state = account_lock_state
        self.account_name = account_name
        self.account_password_valid_time = account_password_valid_time
        self.account_status = account_status
        self.account_type = account_type
        self.database_privileges = database_privileges

    def validate(self):
        if self.database_privileges:
            for v1 in self.database_privileges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_lock_state is not None:
            result['AccountLockState'] = self.account_lock_state

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password_valid_time is not None:
            result['AccountPasswordValidTime'] = self.account_password_valid_time

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        result['DatabasePrivileges'] = []
        if self.database_privileges is not None:
            for k1 in self.database_privileges:
                result['DatabasePrivileges'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountLockState') is not None:
            self.account_lock_state = m.get('AccountLockState')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPasswordValidTime') is not None:
            self.account_password_valid_time = m.get('AccountPasswordValidTime')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        self.database_privileges = []
        if m.get('DatabasePrivileges') is not None:
            for k1 in m.get('DatabasePrivileges'):
                temp_model = main_models.DescribeAccountsZonalResponseBodyAccountsDatabasePrivileges()
                self.database_privileges.append(temp_model.from_map(k1))

        return self

class DescribeAccountsZonalResponseBodyAccountsDatabasePrivileges(DaraModel):
    def __init__(
        self,
        account_privilege: str = None,
        dbname: str = None,
    ):
        self.account_privilege = account_privilege
        self.dbname = dbname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.dbname is not None:
            result['DBName'] = self.dbname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        return self

