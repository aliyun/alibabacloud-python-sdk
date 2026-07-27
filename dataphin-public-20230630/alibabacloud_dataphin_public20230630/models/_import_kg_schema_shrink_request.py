# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportKgSchemaShrinkRequest(DaraModel):
    def __init__(
        self,
        import_command_shrink: str = None,
        op_tenant_id: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.import_command_shrink = import_command_shrink
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
        if self.import_command_shrink is not None:
            result['ImportCommand'] = self.import_command_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportCommand') is not None:
            self.import_command_shrink = m.get('ImportCommand')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

