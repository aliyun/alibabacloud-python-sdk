# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKgEntityRequest(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
        op_tenant_id: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_type = entity_type
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

