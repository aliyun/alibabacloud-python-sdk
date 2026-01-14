# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryWorkspaceRoleConfigRequest(DaraModel):
    def __init__(
        self,
        role_id: int = None,
    ):
        # Workspace role ID, including predefined roles and custom roles:
        # 
        # - 25: Workspace Administrator (predefined role)
        # - 26: Developer (predefined role)
        # - 27: Analyst (predefined role)
        # - 30: Viewer (predefined role)
        # - Custom role: The corresponding role ID for the custom role
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

