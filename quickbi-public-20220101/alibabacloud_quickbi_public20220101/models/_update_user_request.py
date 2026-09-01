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
        # <notice>This parameter has expired and is not recommended. When RoleIds is specified, this parameter does not take effect.</notice>
        self.auth_admin_user = auth_admin_user
        # The intelligent module quota modification information.
        # 
        # Pass the parameter as a JSON array. Each array element contains the following fields:
        # 
        # moduleType -- The intelligent module.
        # - smartQAskNum -- Smart Q questions.
        # - smartQDevNum -- Smart Q building.
        # - qreport -- Smart Q reports.
        # - qExploreNum -- Smart Q exploration edition.
        # 
        # status -- Specifies whether to enable the module.
        # 
        # - 0 -- Revoke authorization.
        # - 1 -- Grant authorization.
        self.copilot_modules = copilot_modules
        # The user status. Valid values:
        # * **false**: Activated.
        # * **true**: Deactivated.
        self.is_deleted = is_deleted
        # The nickname.
        # 
        # - Format check: The maximum length is 50 characters.
        # - Special format check: Chinese characters, English characters, digits, _ \\ / | () ] [
        self.nick_name = nick_name
        # The IDs of preset or custom organization roles to attach to the user, separated by commas (,). A maximum of three role IDs are supported. Valid values:
        # - Organization administrator (preset role): 111111111
        # - Permission management administrator (preset role): 111111112
        # - Common user (preset role): 111111113
        self.role_ids = role_ids
        # The ID of the user to update. This user ID is the Quick BI UserID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The user type of the organization member. Valid values:
        # 
        # - 1: Developer.
        # - 2: Visitor.
        # - 3: Analyst.
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

