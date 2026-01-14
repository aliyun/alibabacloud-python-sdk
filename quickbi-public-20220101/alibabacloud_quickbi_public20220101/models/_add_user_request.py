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
        nick_name: str = None,
        role_ids: str = None,
        user_type: int = None,
    ):
        # Aliyun account ID.
        # >Warning: For versions of Quick BI released after December 31, 2024, AccountId will be a required parameter. Please modify your API before this date.
        # 
        # <props="china">Published only on the China site
        self.account_id = account_id
        # Aliyun account name.
        # 
        # - Note: If it is a sub-account, the format should be \\"primary account: sub-account\\". For example: master_test@aliyun.com:subaccount
        # - Format check: Maximum length of 50 characters.
        self.account_name = account_name
        # Whether to assign the organization administrator role. Value range: 
        # 
        # - true: Yes 
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIds is provided.</notice>
        self.admin_user = admin_user
        # Whether to assign the organization permission administrator role. Value range: 
        # 
        # - true: Yes 
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIds is provided.</notice>
        self.auth_admin_user = auth_admin_user
        # Aliyun account nickname.
        # 
        # - Format check: Maximum length of 50 characters.
        # - Special format validation: Chinese and English characters, numbers, _ \\ / | () ] [
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # Preset or custom organization role IDs bound to the user, separated by commas, with a maximum of 3. Value range:
        # - Organization Administrator (preset role): 111111111
        # - Permission Administrator (preset role): 111111112
        # - Regular User (preset role): 111111113
        self.role_ids = role_ids
        # The user type of the organization member. Value range:
        # - 1: Developer
        # - 2: Visitor
        # - 3: Analyst
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

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

