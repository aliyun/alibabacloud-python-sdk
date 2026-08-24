# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContextDatabaseWorkspaceRequest(DaraModel):
    def __init__(
        self,
        member_name: str = None,
        workspace_name: str = None,
    ):
        # The name of the first member.
        # 
        # This parameter is required.
        self.member_name = member_name
        # The workspace name.
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

