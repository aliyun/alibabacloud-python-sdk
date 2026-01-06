# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWorkspaceDocMembersShrinkRequest(DaraModel):
    def __init__(
        self,
        members_shrink: str = None,
        node_id: str = None,
        tenant_context_shrink: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.members_shrink = members_shrink
        # This parameter is required.
        self.node_id = node_id
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

