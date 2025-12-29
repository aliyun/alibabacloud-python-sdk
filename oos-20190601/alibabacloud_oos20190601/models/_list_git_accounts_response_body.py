# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListGitAccountsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        git_accounts: List[main_models.ListGitAccountsResponseBodyGitAccounts] = None,
        request_id: str = None,
    ):
        self.count = count
        self.git_accounts = git_accounts
        self.request_id = request_id

    def validate(self):
        if self.git_accounts:
            for v1 in self.git_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['GitAccounts'] = []
        if self.git_accounts is not None:
            for k1 in self.git_accounts:
                result['GitAccounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.git_accounts = []
        if m.get('GitAccounts') is not None:
            for k1 in m.get('GitAccounts'):
                temp_model = main_models.ListGitAccountsResponseBodyGitAccounts()
                self.git_accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGitAccountsResponseBodyGitAccounts(DaraModel):
    def __init__(
        self,
        is_active: bool = None,
        owner: str = None,
    ):
        self.is_active = is_active
        self.owner = owner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_active is not None:
            result['IsActive'] = self.is_active

        if self.owner is not None:
            result['Owner'] = self.owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        return self

