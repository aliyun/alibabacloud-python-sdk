# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkspaceUsersRoleRequest(DaraModel):
    def __init__(
        self,
        role_id: int = None,
        user_ids: str = None,
        workspace_id: str = None,
    ):
        # Preset space role ID, existing roles will be overwritten. Value range:
        # - 25: Space Administrator
        # - 26: Space Developer
        # - 27: Space Analyst
        # - 30: Space Viewer
        # 
        # This parameter is required.
        self.role_id = role_id
        # User ID. This is the UserID for Quick BI, not the UID for Alibaba Cloud.
        # 
        # - Supports batch parameters, separate user IDs with a comma (,).
        # 
        # This parameter is required.
        self.user_ids = user_ids
        # Workspace ID.
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

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

