# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataAgentWorkspaceRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        is_session_share_enabled: bool = None,
        workspace_desc: str = None,
        workspace_name: str = None,
    ):
        self.dmsunit = dmsunit
        self.is_session_share_enabled = is_session_share_enabled
        self.workspace_desc = workspace_desc
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

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

