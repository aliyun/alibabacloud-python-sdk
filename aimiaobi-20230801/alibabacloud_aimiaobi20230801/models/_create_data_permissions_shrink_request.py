# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataPermissionsShrinkRequest(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        data_type: str = None,
        permission_user_infos_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.data_id = data_id
        # This parameter is required.
        self.data_type = data_type
        # This parameter is required.
        self.permission_user_infos_shrink = permission_user_infos_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.permission_user_infos_shrink is not None:
            result['PermissionUserInfos'] = self.permission_user_infos_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('PermissionUserInfos') is not None:
            self.permission_user_infos_shrink = m.get('PermissionUserInfos')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

