# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyDentryByNodeIdShrinkRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        name: str = None,
        tenant_context_shrink: str = None,
        to_next_node_id: str = None,
        to_parent_node_id: str = None,
        to_prev_node_id: str = None,
    ):
        # This parameter is required.
        self.dentry_uuid = dentry_uuid
        # This parameter is required.
        self.name = name
        self.tenant_context_shrink = tenant_context_shrink
        self.to_next_node_id = to_next_node_id
        self.to_parent_node_id = to_parent_node_id
        self.to_prev_node_id = to_prev_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.name is not None:
            result['Name'] = self.name

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.to_next_node_id is not None:
            result['ToNextNodeId'] = self.to_next_node_id

        if self.to_parent_node_id is not None:
            result['ToParentNodeId'] = self.to_parent_node_id

        if self.to_prev_node_id is not None:
            result['ToPrevNodeId'] = self.to_prev_node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('ToNextNodeId') is not None:
            self.to_next_node_id = m.get('ToNextNodeId')

        if m.get('ToParentNodeId') is not None:
            self.to_parent_node_id = m.get('ToParentNodeId')

        if m.get('ToPrevNodeId') is not None:
            self.to_prev_node_id = m.get('ToPrevNodeId')

        return self

