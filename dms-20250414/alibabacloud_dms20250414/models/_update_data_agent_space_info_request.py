# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataAgentSpaceInfoRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        is_session_share_enabled: bool = None,
        workspace_desc: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The current DMS unit.
        self.dmsunit = dmsunit
        # Specifies whether to enable session sharing for the workspace. Valid values: true and false.
        self.is_session_share_enabled = is_session_share_enabled
        # The new description for the workspace.
        self.workspace_desc = workspace_desc
        # The ID of the workspace.
        self.workspace_id = workspace_id
        # The new name for the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.is_session_share_enabled is not None:
            result['IsSessionShareEnabled'] = self.is_session_share_enabled

        if self.workspace_desc is not None:
            result['WorkspaceDesc'] = self.workspace_desc

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('IsSessionShareEnabled') is not None:
            self.is_session_share_enabled = m.get('IsSessionShareEnabled')

        if m.get('WorkspaceDesc') is not None:
            self.workspace_desc = m.get('WorkspaceDesc')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

