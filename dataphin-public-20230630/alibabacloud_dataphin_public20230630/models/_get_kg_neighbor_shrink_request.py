# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKgNeighborShrinkRequest(DaraModel):
    def __init__(
        self,
        entity_data_id: str = None,
        entity_type: str = None,
        neighbors_query_shrink: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        workspace_id: str = None,
    ):
        # The entity record data ID.
        # 
        # This parameter is required.
        self.entity_data_id = entity_data_id
        # The entity type.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # The entity record neighbor node query instruction.
        self.neighbors_query_shrink = neighbors_query_shrink
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # The model ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_data_id is not None:
            result['EntityDataId'] = self.entity_data_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.neighbors_query_shrink is not None:
            result['NeighborsQuery'] = self.neighbors_query_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityDataId') is not None:
            self.entity_data_id = m.get('EntityDataId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('NeighborsQuery') is not None:
            self.neighbors_query_shrink = m.get('NeighborsQuery')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

