# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkspaceShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        with_permission_role: bool = None,
        workspace_id: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.with_permission_role = with_permission_role
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.with_permission_role is not None:
            result['WithPermissionRole'] = self.with_permission_role

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WithPermissionRole') is not None:
            self.with_permission_role = m.get('WithPermissionRole')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

