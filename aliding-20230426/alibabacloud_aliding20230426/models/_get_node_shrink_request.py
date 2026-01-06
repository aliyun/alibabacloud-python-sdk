# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNodeShrinkRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        tenant_context_shrink: str = None,
        with_permission_role: bool = None,
        with_statistical_info: bool = None,
    ):
        # This parameter is required.
        self.node_id = node_id
        self.tenant_context_shrink = tenant_context_shrink
        self.with_permission_role = with_permission_role
        self.with_statistical_info = with_statistical_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.with_permission_role is not None:
            result['WithPermissionRole'] = self.with_permission_role

        if self.with_statistical_info is not None:
            result['WithStatisticalInfo'] = self.with_statistical_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WithPermissionRole') is not None:
            self.with_permission_role = m.get('WithPermissionRole')

        if m.get('WithStatisticalInfo') is not None:
            self.with_statistical_info = m.get('WithStatisticalInfo')

        return self

