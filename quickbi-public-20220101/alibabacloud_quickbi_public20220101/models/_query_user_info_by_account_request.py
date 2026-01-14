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
        # Enter the name or ID of the Alibaba Cloud account that you want to query.
        # 
        # *   When you enter an account name:
        # 
        #     *   If the organization user is a master account, such as main_account, the query account format is master account. That is, the main account main_account to be entered.
        #     *   If the organization user is a RAM user, such as a <zhangsan@test.onaliyun.com>, the query account format is the head of the RAM user, that is, the RAM user to be entered is zhangsan.
        # 
        # *   ID:
        # 
        #     *   Enter the UID of the account to query the account information.
        # 
        # This parameter is required.
        self.account = account
        # When a duplicate error occurs while querying the sub-account, enter the primary account\\"s username, for example, zhangsan@test.onaliyun.com.
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

