# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        copilot_modules: str = None,
        nick_name: str = None,
        role_ids: str = None,
        user_type: int = None,
    ):
        # The ID of the Alibaba Cloud account.>Warning: The `AccountId` parameter will be required in Quick BI versions released after December 31, 2024. We recommend that you update your API calls to include this parameter before then.
        self.account_id = account_id
        # The name of the Alibaba Cloud account.
        # 
        # - For a sub-account, use the format `master account:sub-account`. Example: `master_test@aliyun.com:subaccount`.
        # 
        # - The maximum length is 50 characters.
        self.account_name = account_name
        # Specifies whether to assign the organization administrator role. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # >Notice: 
        # 
        # This parameter is deprecated. It is ignored if `RoleIds` is specified.
        self.admin_user = admin_user
        # Specifies whether to assign the permission administrator role. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # >Notice: 
        # 
        # This parameter is deprecated. It is ignored if `RoleIds` is specified.
        self.auth_admin_user = auth_admin_user
        # The Copilot modules to enable for the user. To enable multiple modules, specify their codes separated by a comma (,).
        # 
        # - `qreport`: Q Report
        # 
        # - `qExploreNum`: Q Explore
        # 
        # - `smartQAskNum`: Q\\&A with Data
        # 
        # - `smartQDevNum`: Q-assisted Building
        self.copilot_modules = copilot_modules
        # The user\\"s nickname.
        # 
        # - The maximum length is 50 characters.
        # 
        # - The nickname can contain Chinese characters, letters, digits, and the following special characters: `_ \\ / | () []`.
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The IDs of the predefined or custom organization roles to assign. You can specify up to three role IDs, separated by commas (,). Valid values for predefined roles:
        # 
        # - `111111111`: organization administrator
        # 
        # - `111111112`: permission administrator
        # 
        # - `111111113`: regular user
        self.role_ids = role_ids
        # The type of the organization member. Valid values:
        # 
        # - 1: developer
        # 
        # - 2: viewer
        # 
        # - 3: analyst
        # 
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user

        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user

        if self.copilot_modules is not None:
            result['CopilotModules'] = self.copilot_modules

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')

        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')

        if m.get('CopilotModules') is not None:
            self.copilot_modules = m.get('CopilotModules')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

