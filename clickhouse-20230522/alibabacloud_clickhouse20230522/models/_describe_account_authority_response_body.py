# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountAuthorityResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAccountAuthorityResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
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
            temp_model = main_models.DescribeAccountAuthorityResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountAuthorityResponseBodyData(DaraModel):
    def __init__(
        self,
        account: str = None,
        allow_databases: List[str] = None,
        allow_dictionaries: List[str] = None,
        dbinstance_id: str = None,
        ddl_authority: bool = None,
        dml_authority: int = None,
        total_databases: List[str] = None,
        total_dictionaries: List[str] = None,
    ):
        # The name of the database account.
        self.account = account
        # The list of authorized databases.
        self.allow_databases = allow_databases
        # The list of authorized dictionaries.
        self.allow_dictionaries = allow_dictionaries
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # Indicates whether Data Definition Language (DDL) permissions are granted to the database account. Valid values:
        # 
        # - **true**: DDL is allowed.
        # - **false**: DDL is not allowed.
        self.ddl_authority = ddl_authority
        # Indicates whether Data Manipulation Language (DML) permissions are granted to the database account. Valid values:
        # 
        # - 0: Read, write, and change settings queries are allowed.
        # - 1: Only read data queries are allowed.
        # - 2: Read data and change settings queries are allowed.
        self.dml_authority = dml_authority
        # The list of all databases.
        self.total_databases = total_databases
        # The dictionaries.
        self.total_dictionaries = total_dictionaries

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases

        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority

        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority

        if self.total_databases is not None:
            result['TotalDatabases'] = self.total_databases

        if self.total_dictionaries is not None:
            result['TotalDictionaries'] = self.total_dictionaries

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')

        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')

        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')

        if m.get('TotalDatabases') is not None:
            self.total_databases = m.get('TotalDatabases')

        if m.get('TotalDictionaries') is not None:
            self.total_dictionaries = m.get('TotalDictionaries')

        return self

