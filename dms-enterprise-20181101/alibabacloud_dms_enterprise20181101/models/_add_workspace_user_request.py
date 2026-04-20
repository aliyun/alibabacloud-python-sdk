# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddWorkspaceUserRequest(DaraModel):
    def __init__(
        self,
        dms_user_ids: str = None,
        role_id: str = None,
        role_source: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.dms_user_ids = dms_user_ids
        # This parameter is required.
        self.role_id = role_id
        # This parameter is required.
        self.role_source = role_source
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dms_user_ids is not None:
            result['DmsUserIds'] = self.dms_user_ids

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_source is not None:
            result['RoleSource'] = self.role_source

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DmsUserIds') is not None:
            self.dms_user_ids = m.get('DmsUserIds')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleSource') is not None:
            self.role_source = m.get('RoleSource')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

