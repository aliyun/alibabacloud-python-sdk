# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class DetachHostAccountsFromUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.DetachHostAccountsFromUserGroupResponseBodyResults] = None,
    ):
        # The ID of the request.
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
                temp_model = main_models.DetachHostAccountsFromUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DetachHostAccountsFromUserGroupResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        host_accounts: List[main_models.DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts] = None,
        host_id: str = None,
        message: str = None,
        user_group_id: str = None,
    ):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The result of revoking permissions on the specified host accounts from the user group.
        self.host_accounts = host_accounts
        # The ID of the host.
        self.host_id = host_id
        # This parameter is deprecated.
        self.message = message
        # The ID of the group.
        self.user_group_id = user_group_id

    def validate(self):
        if self.host_accounts:
            for v1 in self.host_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k1 in self.host_accounts:
                result['HostAccounts'].append(k1.to_map() if k1 else None)

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.message is not None:
            result['Message'] = self.message

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k1 in m.get('HostAccounts'):
                temp_model = main_models.DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k1))

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

class DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts(DaraModel):
    def __init__(
        self,
        code: str = None,
        host_account_id: str = None,
        message: str = None,
    ):
        # The return code that indicates whether permissions on the specified host account were revoked from the user group. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code
        # The ID of the host account.
        self.host_account_id = host_account_id
        # This parameter is deprecated.
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

        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

