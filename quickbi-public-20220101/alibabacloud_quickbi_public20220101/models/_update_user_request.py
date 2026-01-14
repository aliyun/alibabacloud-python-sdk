# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        is_deleted: bool = None,
        nick_name: str = None,
        role_ids: str = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # Indicates whether the organization administrator. Valid values:
        # 
        # *   true
        # *   false
        self.admin_user = admin_user
        # Indicate whether the RAM user is a permission administrator. Valid values:
        # 
        # *   true
        # *   false
        self.auth_admin_user = auth_admin_user
        # User status: 
        # * **false**: Active
        #  * **true**: Inactive
        self.is_deleted = is_deleted
        # The nickname of the account.
        # 
        # *   Format check: The value can be up to 50 characters in length.
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        self.nick_name = nick_name
        # The IDs of the preset or custom organization roles bound to the user, separated by English commas \\",\\", with a maximum of 3. The value range is as follows: - Organization Administrator (preset role): 111111111 - Permission Administrator (preset role): 111111112 - Regular User (preset role): 111111113
        self.role_ids = role_ids
        # The ID of the user to be updated. The user ID is the UserID of the Quick BI, not the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The type of user who is a member of the organization. Valid values:
        # 
        # *   1 : developer
        # *   2 : visitors
        # *   3 : Analyst
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

