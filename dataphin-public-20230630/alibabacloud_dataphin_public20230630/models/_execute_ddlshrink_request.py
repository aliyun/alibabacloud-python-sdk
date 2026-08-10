# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteDDLShrinkRequest(DaraModel):
    def __init__(
        self,
        context_shrink: str = None,
        ddlcommand_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # The request context information.
        # 
        # This parameter is required.
        self.context_shrink = context_shrink
        # The one-click table creation parameters.
        # 
        # This parameter is required.
        self.ddlcommand_shrink = ddlcommand_shrink
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_shrink is not None:
            result['Context'] = self.context_shrink

        if self.ddlcommand_shrink is not None:
            result['DDLCommand'] = self.ddlcommand_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context_shrink = m.get('Context')

        if m.get('DDLCommand') is not None:
            self.ddlcommand_shrink = m.get('DDLCommand')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

