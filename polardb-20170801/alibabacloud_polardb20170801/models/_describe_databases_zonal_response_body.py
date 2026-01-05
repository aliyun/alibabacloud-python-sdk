# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabasesZonalResponseBody(DaraModel):
    def __init__(
        self,
        databases: List[main_models.DescribeDatabasesZonalResponseBodyDatabases] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
    ):
        self.databases = databases
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id

    def validate(self):
        if self.databases:
            for v1 in self.databases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Databases'] = []
        if self.databases is not None:
            for k1 in self.databases:
                result['Databases'].append(k1.to_map() if k1 else None)

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
        self.databases = []
        if m.get('Databases') is not None:
            for k1 in m.get('Databases'):
                temp_model = main_models.DescribeDatabasesZonalResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k1))

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

class DescribeDatabasesZonalResponseBodyDatabases(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.DescribeDatabasesZonalResponseBodyDatabasesAccounts] = None,
        character_set_name: str = None,
        dbdescription: str = None,
        dbname: str = None,
        dbstatus: str = None,
        engine: str = None,
        master_id: str = None,
    ):
        self.accounts = accounts
        self.character_set_name = character_set_name
        self.dbdescription = dbdescription
        self.dbname = dbname
        self.dbstatus = dbstatus
        self.engine = engine
        self.master_id = master_id

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
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.DescribeDatabasesZonalResponseBodyDatabasesAccounts()
                self.accounts.append(temp_model.from_map(k1))

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

class DescribeDatabasesZonalResponseBodyDatabasesAccounts(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        account_status: str = None,
        privilege_status: str = None,
    ):
        self.account_name = account_name
        self.account_privilege = account_privilege
        self.account_status = account_status
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

