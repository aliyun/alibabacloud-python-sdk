# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPipelineByIdShrinkRequest(DaraModel):
    def __init__(
        self,
        context_shrink: str = None,
        op_tenant_id: int = None,
        query_id_shrink: str = None,
    ):
        # This parameter is required.
        self.context_shrink = context_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.query_id_shrink = query_id_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_shrink is not None:
            result['Context'] = self.context_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.query_id_shrink is not None:
            result['QueryId'] = self.query_id_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context_shrink = m.get('Context')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('QueryId') is not None:
            self.query_id_shrink = m.get('QueryId')

        return self

