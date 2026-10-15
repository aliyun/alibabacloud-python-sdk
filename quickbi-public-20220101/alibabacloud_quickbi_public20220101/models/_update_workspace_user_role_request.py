# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkspaceUserRoleRequest(DaraModel):
    def __init__(
        self,
        role_id: int = None,
        role_ids: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The preset workspace role ID. The existing role is overwritten. Valid values:
        # - 25: workspace administrator
        # - 26: workspace developer
        # - 27: workspace analyst
        # - 30: workspace viewer
        self.role_id = role_id
        # Multiple workspace role IDs, separated by commas. If this parameter is specified, it takes precedence.
        # >Notice: roleId and roleIds cannot both be empty
        self.role_ids = role_ids
        # The Quick BI user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

