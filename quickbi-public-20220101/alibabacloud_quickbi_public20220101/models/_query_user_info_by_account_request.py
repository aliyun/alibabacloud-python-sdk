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
        # The Alibaba Cloud account name or Alibaba Cloud ID to query.
        # - When you enter an account name:
        #     - If the organization user is a primary account (for example, main_account), the query account format is the primary account. That is, enter the primary account main_account. 
        #     - If the organization user is a RAM user (for example, zhangsan@test.onaliyun.com), the query account format is the prefix of the RAM user. That is, enter zhangsan.
        # - When you enter an Alibaba Cloud ID:
        #     - Enter the complete account UID to query the corresponding account information.
        # 
        # This parameter is required.
        self.account = account
        # The account name of the primary account when a duplicate error occurs during RAM user query. For example, zhangsan@test.onaliyun.com.
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

