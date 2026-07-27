# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKgRelationRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        relation_id: str = None,
        relation_type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.relation_id = relation_id
        # This parameter is required.
        self.relation_type = relation_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

