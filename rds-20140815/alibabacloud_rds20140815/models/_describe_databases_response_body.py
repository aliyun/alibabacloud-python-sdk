# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        databases: main_models.DescribeDatabasesResponseBodyDatabases = None,
        request_id: str = None,
    ):
        # The information about the databases.
        self.databases = databases
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabases()
            self.databases = temp_model.from_map(m.get('Databases'))

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
        advanced_info: main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAdvancedInfo = None,
        basic_info: main_models.DescribeDatabasesResponseBodyDatabasesDatabaseBasicInfo = None,
        character_set_name: str = None,
        collate: str = None,
        conn_limit: str = None,
        ctype: str = None,
        dbdescription: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        dbstatus: str = None,
        duck_dbenabled: bool = None,
        engine: str = None,
        page_number: int = None,
        page_size: int = None,
        runtime_info: main_models.DescribeDatabasesResponseBodyDatabasesDatabaseRuntimeInfo = None,
        tablespace: str = None,
        total_count: int = None,
    ):
        # The information about the account. Each account has specific permissions on the database.
        self.accounts = accounts
        # The advanced information about the database.
        # 
        # >  This parameter is returned only for instances that run SQL Server.
        self.advanced_info = advanced_info
        # The basic information about the database.
        # 
        # >  This parameter is returned only for instances that run SQL Server.
        self.basic_info = basic_info
        # The name of the character set.
        self.character_set_name = character_set_name
        # The collation of the character set. The example value C indicates localization.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.collate = collate
        # The limit on the number of concurrent requests. The value -1 indicates that the number of concurrent requests is unlimited.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.conn_limit = conn_limit
        # The type of the character set.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.ctype = ctype
        # The description of the database.
        self.dbdescription = dbdescription
        # The ID of the instance to which the database belongs.
        self.dbinstance_id = dbinstance_id
        # The database name.
        self.dbname = dbname
        # The database status. Valid values:
        # 
        # *   **Creating**
        # *   **Running**
        # *   **Deleting**
        # *   **Cold**
        self.dbstatus = dbstatus
        self.duck_dbenabled = duck_dbenabled
        # The database engine of the instance.
        self.engine = engine
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The runtime information about the database.
        # 
        # >  This parameter is returned only for instances that run SQL Server.
        self.runtime_info = runtime_info
        # The database tablespace.
        # 
        # >  This parameter is returned only for instances that run PostgreSQL.
        self.tablespace = tablespace
        # The total number of entries returned.
        # 
        # >  This parameter is returned only for instances that run SQL Server.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()
        if self.advanced_info:
            self.advanced_info.validate()
        if self.basic_info:
            self.basic_info.validate()
        if self.runtime_info:
            self.runtime_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()

        if self.advanced_info is not None:
            result['AdvancedInfo'] = self.advanced_info.to_map()

        if self.basic_info is not None:
            result['BasicInfo'] = self.basic_info.to_map()

        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        if self.collate is not None:
            result['Collate'] = self.collate

        if self.conn_limit is not None:
            result['ConnLimit'] = self.conn_limit

        if self.ctype is not None:
            result['Ctype'] = self.ctype

        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbstatus is not None:
            result['DBStatus'] = self.dbstatus

        if self.duck_dbenabled is not None:
            result['DuckDBEnabled'] = self.duck_dbenabled

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.runtime_info is not None:
            result['RuntimeInfo'] = self.runtime_info.to_map()

        if self.tablespace is not None:
            result['Tablespace'] = self.tablespace

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('AdvancedInfo') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAdvancedInfo()
            self.advanced_info = temp_model.from_map(m.get('AdvancedInfo'))

        if m.get('BasicInfo') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabaseBasicInfo()
            self.basic_info = temp_model.from_map(m.get('BasicInfo'))

        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        if m.get('Collate') is not None:
            self.collate = m.get('Collate')

        if m.get('ConnLimit') is not None:
            self.conn_limit = m.get('ConnLimit')

        if m.get('Ctype') is not None:
            self.ctype = m.get('Ctype')

        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBStatus') is not None:
            self.dbstatus = m.get('DBStatus')

        if m.get('DuckDBEnabled') is not None:
            self.duck_dbenabled = m.get('DuckDBEnabled')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuntimeInfo') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabaseRuntimeInfo()
            self.runtime_info = temp_model.from_map(m.get('RuntimeInfo'))

        if m.get('Tablespace') is not None:
            self.tablespace = m.get('Tablespace')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDatabasesResponseBodyDatabasesDatabaseRuntimeInfo(DaraModel):
    def __init__(
        self,
        runtime_db_property: List[Dict[str, Any]] = None,
    ):
        self.runtime_db_property = runtime_db_property

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.runtime_db_property is not None:
            result['RuntimeDbProperty'] = self.runtime_db_property

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuntimeDbProperty') is not None:
            self.runtime_db_property = m.get('RuntimeDbProperty')

        return self

class DescribeDatabasesResponseBodyDatabasesDatabaseBasicInfo(DaraModel):
    def __init__(
        self,
        basic_db_property: List[Dict[str, Any]] = None,
    ):
        self.basic_db_property = basic_db_property

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_db_property is not None:
            result['BasicDbProperty'] = self.basic_db_property

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicDbProperty') is not None:
            self.basic_db_property = m.get('BasicDbProperty')

        return self

class DescribeDatabasesResponseBodyDatabasesDatabaseAdvancedInfo(DaraModel):
    def __init__(
        self,
        advanced_db_property: List[Dict[str, Any]] = None,
    ):
        self.advanced_db_property = advanced_db_property

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_db_property is not None:
            result['AdvancedDbProperty'] = self.advanced_db_property

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedDbProperty') is not None:
            self.advanced_db_property = m.get('AdvancedDbProperty')

        return self

class DescribeDatabasesResponseBodyDatabasesDatabaseAccounts(DaraModel):
    def __init__(
        self,
        account_privilege_info: List[main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccountPrivilegeInfo] = None,
    ):
        self.account_privilege_info = account_privilege_info

    def validate(self):
        if self.account_privilege_info:
            for v1 in self.account_privilege_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountPrivilegeInfo'] = []
        if self.account_privilege_info is not None:
            for k1 in self.account_privilege_info:
                result['AccountPrivilegeInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_privilege_info = []
        if m.get('AccountPrivilegeInfo') is not None:
            for k1 in m.get('AccountPrivilegeInfo'):
                temp_model = main_models.DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccountPrivilegeInfo()
                self.account_privilege_info.append(temp_model.from_map(k1))

        return self

class DescribeDatabasesResponseBodyDatabasesDatabaseAccountsAccountPrivilegeInfo(DaraModel):
    def __init__(
        self,
        account: str = None,
        account_privilege: str = None,
        account_privilege_detail: str = None,
    ):
        # The account username.
        self.account = account
        # The permissions that the account has on the database. Valid values:
        # 
        # *   **ReadWrite**: read and write permissions
        # *   **ReadOnly**: read-only permissions
        # *   **DMLOnly**: DML-only permissions
        # *   **DDLOnly**: DDL-only permissions
        self.account_privilege = account_privilege
        # The permission that the account has on the database.
        self.account_privilege_detail = account_privilege_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.account_privilege_detail is not None:
            result['AccountPrivilegeDetail'] = self.account_privilege_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('AccountPrivilegeDetail') is not None:
            self.account_privilege_detail = m.get('AccountPrivilegeDetail')

        return self

