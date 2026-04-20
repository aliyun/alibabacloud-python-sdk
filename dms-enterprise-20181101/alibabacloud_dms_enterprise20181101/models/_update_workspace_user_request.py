# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkspaceUserRequest(DaraModel):
    def __init__(
        self,
        dms_user_id: str = None,
        role_ids: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.dms_user_id = dms_user_id
        # This parameter is required.
        self.role_ids = role_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dms_user_id is not None:
            result['DmsUserId'] = self.dms_user_id

        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DmsUserId') is not None:
            self.dms_user_id = m.get('DmsUserId')

        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

