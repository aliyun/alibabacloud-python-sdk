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
        # The Alibaba Cloud account ID.
        # >Warning: For Quick BI versions released after December 31, 2024, AccountId is a required parameter. Update your API calls before this date.
        self.account_id = account_id
        # The Alibaba Cloud account name.
        # 
        # - Note: For a RAM user, the format is "primary account:RAM user". Example: master_test@aliyun.com:subaccount
        # - Format check: The maximum length is 50 characters.
        self.account_name = account_name
        # Specifies whether to assign the organization administrator role. Valid values: 
        # 
        # - true: Yes. 
        # - false: No.
        # 
        # <notice>This parameter is deprecated. When RoleIds is specified, this parameter does not take effect.</notice>
        self.admin_user = admin_user
        # Specifies whether to assign the organization permission management administrator role. Valid values: 
        # 
        # - true: Yes. 
        # - false: No.
        # 
        # <notice>This parameter has expired and is no longer recommended. When RoleIds is specified, this parameter does not take effect.</notice>
        self.auth_admin_user = auth_admin_user
        # The intelligent module quotas of the user. Separate multiple modules with commas (,).
        # 
        # - qreport -- Small Q Report
        # - qExploreNum -- Small Q Explorer
        # - smartQAskNum -- Small Q Ask
        # - smartQDevNum -- Small Q Builder
        self.copilot_modules = copilot_modules
        # The nickname of the Alibaba Cloud account.
        # 
        # - Format check: The maximum length is 50 characters.
        # - Special character validation: Chinese characters, English characters, digits, _ \\ / | () ] [
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The IDs of preset or custom organization roles to attach to the user, separated by commas (,). A maximum of three role IDs are supported. Valid values:
        # - Organization administrator (preset role): 111111111
        # - Permission management administrator (preset role): 111111112
        # - Common user (preset role): 111111113
        self.role_ids = role_ids
        # The user type of the organization member. Valid values:
        # - 1: Developer.
        # - 2: Visitor.
        # - 3: Analyst.
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

