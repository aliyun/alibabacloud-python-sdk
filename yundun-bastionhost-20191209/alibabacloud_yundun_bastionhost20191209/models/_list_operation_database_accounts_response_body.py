# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListOperationDatabaseAccountsResponseBody(DaraModel):
    def __init__(
        self,
        database_accounts: List[main_models.ListOperationDatabaseAccountsResponseBodyDatabaseAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The database accounts returned.
        self.database_accounts = database_accounts
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.database_accounts:
            for v1 in self.database_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k1 in self.database_accounts:
                result['DatabaseAccounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k1 in m.get('DatabaseAccounts'):
                temp_model = main_models.ListOperationDatabaseAccountsResponseBodyDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOperationDatabaseAccountsResponseBodyDatabaseAccounts(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        database_account_id: str = None,
        database_account_name: str = None,
        database_id: str = None,
        has_password: str = None,
        login_attribute: str = None,
        protocol_name: str = None,
    ):
        # The name of the PostgreSQL or Oracle database.
        self.dbname = dbname
        # The database account ID.
        self.database_account_id = database_account_id
        # The name of the database account.
        self.database_account_name = database_account_name
        # The database ID.
        self.database_id = database_id
        # Indicates whether a password is configured for the database host account.
        self.has_password = has_password
        # The logon attribute. One of the following values is returned if the database engine is Oracle:
        # 
        # *   **SERVICENAME**
        # *   **SID**
        self.login_attribute = login_attribute
        # The protocol that is used by the database account.
        self.protocol_name = protocol_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id

        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.has_password is not None:
            result['HasPassword'] = self.has_password

        if self.login_attribute is not None:
            result['LoginAttribute'] = self.login_attribute

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')

        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')

        if m.get('LoginAttribute') is not None:
            self.login_attribute = m.get('LoginAttribute')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        return self

