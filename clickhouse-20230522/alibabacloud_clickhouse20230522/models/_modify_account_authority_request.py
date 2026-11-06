# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class ModifyAccountAuthorityRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        dml_auth_setting: main_models.ModifyAccountAuthorityRequestDmlAuthSetting = None,
        region_id: str = None,
    ):
        # The database account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The authorization information.
        # 
        # This parameter is required.
        self.dml_auth_setting = dml_auth_setting
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.dml_auth_setting:
            self.dml_auth_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dml_auth_setting is not None:
            result['DmlAuthSetting'] = self.dml_auth_setting.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DmlAuthSetting') is not None:
            temp_model = main_models.ModifyAccountAuthorityRequestDmlAuthSetting()
            self.dml_auth_setting = temp_model.from_map(m.get('DmlAuthSetting'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyAccountAuthorityRequestDmlAuthSetting(DaraModel):
    def __init__(
        self,
        allow_databases: List[str] = None,
        allow_dictionaries: List[str] = None,
        ddl_authority: bool = None,
        dml_authority: int = None,
    ):
        # The list of databases to be authorized. Separate multiple databases with commas (,).
        self.allow_databases = allow_databases
        # The list of dictionaries to be authorized. Separate multiple dictionaries with commas (,).
        self.allow_dictionaries = allow_dictionaries
        # Specifies whether to grant DDL permissions to the database account. Valid values:
        # 
        # - **true**: DDL is allowed.
        # - **false**: DDL is not allowed.
        # 
        # This parameter is required.
        self.ddl_authority = ddl_authority
        # Specifies whether to grant DML permissions to the database account. Valid values:
        # 
        # - **0**: Read, write, and change settings queries are allowed.
        # 
        # - **1**: Only read data queries are allowed.
        # 
        # - **2**: Read data and change settings queries are allowed.
        # 
        # This parameter is required.
        self.dml_authority = dml_authority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_databases is not None:
            result['AllowDatabases'] = self.allow_databases

        if self.allow_dictionaries is not None:
            result['AllowDictionaries'] = self.allow_dictionaries

        if self.ddl_authority is not None:
            result['DdlAuthority'] = self.ddl_authority

        if self.dml_authority is not None:
            result['DmlAuthority'] = self.dml_authority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowDatabases') is not None:
            self.allow_databases = m.get('AllowDatabases')

        if m.get('AllowDictionaries') is not None:
            self.allow_dictionaries = m.get('AllowDictionaries')

        if m.get('DdlAuthority') is not None:
            self.ddl_authority = m.get('DdlAuthority')

        if m.get('DmlAuthority') is not None:
            self.dml_authority = m.get('DmlAuthority')

        return self

