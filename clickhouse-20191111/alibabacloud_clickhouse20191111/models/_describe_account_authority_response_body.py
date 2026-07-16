# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAccountAuthorityResponseBody(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        allow_databases: List[str] = None,
        allow_dictionaries: List[str] = None,
        ddl_authority: bool = None,
        dml_authority: str = None,
        request_id: str = None,
        total_databases: List[str] = None,
        total_dictionaries: List[str] = None,
    ):
        # The database account name.
        self.account_name = account_name
        # The list of authorized databases.
        self.allow_databases = allow_databases
        # The list of authorized dictionaries.
        self.allow_dictionaries = allow_dictionaries
        # Indicates whether the account has DDL permissions. Valid values:
        # 
        # - **true**: DDL permissions are granted.
        # 
        # - **false**: DDL permissions are denied.
        self.ddl_authority = ddl_authority
        # The DML permission level for the account. Valid values:
        # 
        # - **all**: read, write, and settings permissions.
        # 
        # - **readOnly,modify**: read and settings permissions.
        self.dml_authority = dml_authority
        # The request ID.
        self.request_id = request_id
        # A list of all databases in the cluster.
        self.total_databases = total_databases
        # A list of all dictionaries in the cluster.
        self.total_dictionaries = total_dictionaries

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases

        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries

        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority

        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_databases is not None:
            result['TotalDatabases'] = self.total_databases

        if self.total_dictionaries is not None:
            result['TotalDictionaries'] = self.total_dictionaries

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')

        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')

        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')

        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalDatabases') is not None:
            self.total_databases = m.get('TotalDatabases')

        if m.get('TotalDictionaries') is not None:
            self.total_dictionaries = m.get('TotalDictionaries')

        return self

