# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkspaceRoleUsersRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        role_id: int = None,
        workspace_id: str = None,
    ):
        # Keyword for the user\\"s nickname.
        self.keyword = keyword
        # Current page number for pagination:
        # 
        # - Starting value: 1
        # - Default value: 1
        self.page_num = page_num
        # Number of items per page for pagination:
        # 
        # - Default value: 10
        # - Maximum value: 1000
        self.page_size = page_size
        # Workspace role ID, including predefined roles and custom roles:
        # 
        # - 25: Workspace Administrator (predefined role)
        # - 26: Developer (predefined role)
        # - 27: Analyst (predefined role)
        # - 30: Viewer (predefined role)
        # - Custom roles: The corresponding role ID for custom roles
        # 
        # This parameter is required.
        self.role_id = role_id
        # The ID of the workspace. This parameter is optional. If you do not set this parameter, the roles of all workspaces are returned.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

