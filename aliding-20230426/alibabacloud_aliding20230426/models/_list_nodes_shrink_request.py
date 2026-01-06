# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        parent_node_id: str = None,
        tenant_context_shrink: str = None,
        with_permission_role: bool = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.parent_node_id = parent_node_id
        self.tenant_context_shrink = tenant_context_shrink
        self.with_permission_role = with_permission_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.with_permission_role is not None:
            result['WithPermissionRole'] = self.with_permission_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WithPermissionRole') is not None:
            self.with_permission_role = m.get('WithPermissionRole')

        return self

