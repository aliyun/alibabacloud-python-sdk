# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetDatabaseAccountResponseBody(DaraModel):
    def __init__(
        self,
        database_account: main_models.GetDatabaseAccountResponseBodyDatabaseAccount = None,
        request_id: str = None,
    ):
        # The returned information about the database account.
        self.database_account = database_account
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.database_account:
            self.database_account.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_account is not None:
            result['DatabaseAccount'] = self.database_account.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccount') is not None:
            temp_model = main_models.GetDatabaseAccountResponseBodyDatabaseAccount()
            self.database_account = temp_model.from_map(m.get('DatabaseAccount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDatabaseAccountResponseBodyDatabaseAccount(DaraModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_schema: str = None,
        has_password: bool = None,
        login_attribute: str = None,
    ):
        # The database account ID.
        self.database_account_id = database_account_id
        # The name of the database account.
        self.database_account_name = database_account_name
        # The database name. A value is returned for this parameter if the database engine is PostgreSQL or Oracle.
        self.database_schema = database_schema
        # Indicates whether the database account has a password.
        # Valid values:
        # * true
        # * false
        self.has_password = has_password
        # The logon attribute. A value is returned for this parameter if the database engine is Oracle. Valid values:
        # 
        # *   SERVICENAME
        # *   SID
        self.login_attribute = login_attribute

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

        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema

        if self.has_password is not None:
            result['HasPassword'] = self.has_password

        if self.login_attribute is not None:
            result['LoginAttribute'] = self.login_attribute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')

        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')

        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')

        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')

        if m.get('LoginAttribute') is not None:
            self.login_attribute = m.get('LoginAttribute')

        return self

