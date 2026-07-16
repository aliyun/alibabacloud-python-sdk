# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserInfoByAccountRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        parent_account_name: str = None,
    ):
        # The Alibaba Cloud account name or Alibaba Cloud ID of the user.
        # 
        # - If you enter an account name:
        # 
        #   - If the organization member is a root account, such as `main_account`, enter the root account name. For example, `main_account`.
        # 
        #   - If the organization member is a RAM user, such as `zhangsan@test.onaliyun.com`, enter the prefix of the username before the at sign (@). For example, `zhangsan`.
        # 
        # - If you enter an Alibaba Cloud ID:
        # 
        #   - Enter the complete user ID (UID) of the account.
        # 
        # This parameter is required.
        self.account = account
        # To resolve a "duplicate user" error when querying a RAM user, specify the name of the root account to which the user belongs.
        self.parent_account_name = parent_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.parent_account_name is not None:
            result['ParentAccountName'] = self.parent_account_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('ParentAccountName') is not None:
            self.parent_account_name = m.get('ParentAccountName')

        return self

