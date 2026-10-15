# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddWorkspaceUsersRequest(DaraModel):
    def __init__(
        self,
        role_id: int = None,
        user_ids: str = None,
        workspace_id: str = None,
    ):
        # The ID of the preset workspace role. Valid values:
        # - 25: storage management administrator
        # - 26: workspace developer
        # - 27: storage analysis analyst
        # - 30: workspace viewer
        # 
        # This parameter is required.
        self.role_id = role_id
        # The user IDs. These are Quick BI user IDs, not Alibaba Cloud UIDs.
        # 
        # - You can pass multiple user IDs separated by commas (,).
        # 
        # This parameter is required.
        self.user_ids = user_ids
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

