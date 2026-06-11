# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        copilot_modules: str = None,
        is_deleted: bool = None,
        nick_name: str = None,
        role_ids: str = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # Whether to assign the organization administrator role to the user. Valid values:
        # 
        # - `true`
        # 
        # - `false`
        # 
        # >Notice: 
        # 
        # This parameter is deprecated and is ignored if RoleIds is also specified.
        self.admin_user = admin_user
        # Whether to assign the permission administrator role to the user. Valid values:
        # 
        # - `true`
        # 
        # - `false`
        # 
        # >Notice: 
        # 
        # This parameter is deprecated and is ignored if RoleIds is also specified.
        self.auth_admin_user = auth_admin_user
        self.copilot_modules = copilot_modules
        # The user status:
        # 
        # - **`false`**: active
        # 
        # - **`true`**: inactive
        self.is_deleted = is_deleted
        # The nickname of the user.
        # 
        # - The nickname can be up to 50 characters in length.
        # 
        # - The nickname can contain Chinese characters, letters, digits, and the following special characters: `_ \\ / | () ] [`
        self.nick_name = nick_name
        # The IDs of the built-in or custom organization roles to assign to the user. Specify up to three comma-separated role IDs.
        # 
        # - organization administrator (built-in role): 111111111
        # 
        # - permission administrator (built-in role): 111111112
        # 
        # - standard user (built-in role): 111111113
        self.role_ids = role_ids
        # The ID of the Quick BI user to update. This is not an Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The user type of the organization member. Valid values:
        # 
        # - `1`: developer
        # 
        # - `2`: viewer
        # 
        # - `3`: analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user

        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user

        if self.copilot_modules is not None:
            result['CopilotModules'] = self.copilot_modules

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')

        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')

        if m.get('CopilotModules') is not None:
            self.copilot_modules = m.get('CopilotModules')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

