# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListDatabaseAccountsResponseBody(DaraModel):
    def __init__(
        self,
        database_accounts: List[main_models.ListDatabaseAccountsResponseBodyDatabaseAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned database accounts.
        self.database_accounts = database_accounts
        # The request ID.
        self.request_id = request_id
        # The total number of database accounts returned.
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
                temp_model = main_models.ListDatabaseAccountsResponseBodyDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDatabaseAccountsResponseBodyDatabaseAccounts(DaraModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_id: str = None,
        database_schema: str = None,
        has_password: str = None,
    ):
        # The database account ID.
        self.database_account_id = database_account_id
        # The name of the database account.
        self.database_account_name = database_account_name
        # The database ID.
        self.database_id = database_id
        # The name of the database. A value is returned for this parameter if the engine of the database with the specified database ID is PostgreSQL or Oracle.
        self.database_schema = database_schema
        # Indicates whether the database account has a password. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.has_password = has_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id

        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema

        if self.has_password is not None:
            result['HasPassword'] = self.has_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')

        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')

        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')

        return self

