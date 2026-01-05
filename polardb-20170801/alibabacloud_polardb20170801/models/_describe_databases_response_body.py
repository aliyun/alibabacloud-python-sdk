# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        databases: main_models.DescribeDatabasesResponseBodyDatabases = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
    ):
        # Details about databases.
        self.databases = databases
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.databases:
            self.databases.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabases()
            self.databases = temp_model.from_map(m.get('Databases'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDatabasesResponseBodyDatabases(DaraModel):
    def __init__(
        self,
        database: List[main_models.DescribeDatabasesResponseBodyDatabasesDatabase] = None,
    ):
        self.database = database

    def validate(self):
        if self.database:
            for v1 in self.database:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Database'] = []
        if self.database is not None:
            for k1 in self.database:
                result['Database'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database = []
        if m.get('Database') is not None:
            for k1 in m.get('Database'):
                temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabase()
                self.database.append(temp_model.from_map(k1))

        return self

class DescribeDatabasesResponseBodyDatabasesDatabase(DaraModel):
    def __init__(
        self,
        accounts: main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAccounts = None,
        character_set_name: str = None,
        dbdescription: str = None,
        dbname: str = None,
        dbstatus: str = None,
        engine: str = None,
        master_id: str = None,
    ):
        # Details about the accounts.
        # 
        # > A PolarDB for MySQL cluster does not support privileged accounts.
        self.accounts = accounts
        # The character set that the database uses. For more information, see [Character set tables](https://help.aliyun.com/document_detail/99716.html).
        self.character_set_name = character_set_name
        # The description of the database.
        self.dbdescription = dbdescription
        # The name of the database.
        self.dbname = dbname
        # The state of the database. Valid values:
        # 
        # *   **Creating**
        # *   **Running**
        # *   **Deleting**
        self.dbstatus = dbstatus
        # The type of the database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **Oracle**
        # *   **PostgreSQL**
        self.engine = engine
        # The ID of the primary node in the cluster of Multi-master Cluster (Database/Table) Edition.
        self.master_id = master_id

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

        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbstatus is not None:
            result['DBStatus'] = self.dbstatus

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.master_id is not None:
            result['MasterID'] = self.master_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBStatus') is not None:
            self.dbstatus = m.get('DBStatus')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('MasterID') is not None:
            self.master_id = m.get('MasterID')

        return self

class DescribeDatabasesResponseBodyDatabasesDatabaseAccounts(DaraModel):
    def __init__(
        self,
        account: List[main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccount] = None,
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
                temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccount()
                self.account.append(temp_model.from_map(k1))

        return self

class DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccount(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        account_status: str = None,
        privilege_status: str = None,
    ):
        # The username of the account.
        # 
        # > A PolarDB for MySQL cluster does not support privileged accounts.
        self.account_name = account_name
        # The permissions that are granted to the account. Valid values:
        # 
        # *   **ReadWrite**: read and write permissions
        # *   **ReadOnly**: read-only permissions
        # *   **DMLOnly**: The account is granted the permissions to execute only DML statements on the database.
        # *   **DDLOnly**: The account is granted the permissions to execute only DDL statements on the database.
        # *   **ReadIndex**: The account has the read and index permissions on the database.
        self.account_privilege = account_privilege
        # The state of the account. Valid values:
        # 
        # *   **Creating**
        # *   **Available**
        # *   **Deleting**
        self.account_status = account_status
        # The authorization state of the account. Valid values:
        # 
        # *   **Empowering**: The system is granting permissions to the account.
        # *   **Empowered**: Permissions are granted to the account.
        # *   **Removing**: The system is revoking permissions from the account.
        self.privilege_status = privilege_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.privilege_status is not None:
            result['PrivilegeStatus'] = self.privilege_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('PrivilegeStatus') is not None:
            self.privilege_status = m.get('PrivilegeStatus')

        return self

