# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserToWorkspaceRequest(DaraModel):
    def __init__(
        self,
        role_id: int = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The preset space role ID. Value range:
        # - 25: Space Administrator
        # - 26: Space Developer
        # - 27: Space Analyst
        # - 30: Space Viewer
        # 
        # This parameter is required.
        self.role_id = role_id
        # The ID of the Quick BI user to be added.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The ID of the workspace.
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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

