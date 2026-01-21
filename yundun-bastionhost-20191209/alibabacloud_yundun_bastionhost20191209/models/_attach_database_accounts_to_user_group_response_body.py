# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class AttachDatabaseAccountsToUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.AttachDatabaseAccountsToUserGroupResponseBodyResults] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result of the call.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.AttachDatabaseAccountsToUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class AttachDatabaseAccountsToUserGroupResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        database_accounts: List[main_models.AttachDatabaseAccountsToUserGroupResponseBodyResultsDatabaseAccounts] = None,
        database_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        # The error code returned. If OK is returned, the authorization was successful. If another error code is returned, the authorization failed.
        self.code = code
        # A list that shows the authorization results of the database accounts.
        self.database_accounts = database_accounts
        # The database ID.
        self.database_id = database_id
        # The error message returned.
        self.message = message
        # The user group ID.
        self.user_group_id = user_group_id

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
        if self.code is not None:
            result['Code'] = self.code

        result['DatabaseAccounts'] = []
        if self.database_accounts is not None:
            for k1 in self.database_accounts:
                result['DatabaseAccounts'].append(k1.to_map() if k1 else None)

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.message is not None:
            result['Message'] = self.message

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.database_accounts = []
        if m.get('DatabaseAccounts') is not None:
            for k1 in m.get('DatabaseAccounts'):
                temp_model = main_models.AttachDatabaseAccountsToUserGroupResponseBodyResultsDatabaseAccounts()
                self.database_accounts.append(temp_model.from_map(k1))

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

class AttachDatabaseAccountsToUserGroupResponseBodyResultsDatabaseAccounts(DaraModel):
    def __init__(
        self,
        code: str = None,
        database_account_id: str = None,
        message: str = None,
    ):
        # The error code returned. If OK is returned, the authorization was successful. If another error code is returned, the authorization failed.
        self.code = code
        # The database account ID.
        self.database_account_id = database_account_id
        # The error message returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

