# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPipelineAsyncResultShrinkRequest(DaraModel):
    def __init__(
        self,
        async_id: int = None,
        context_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.async_id = async_id
        # This parameter is required.
        self.context_shrink = context_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_id is not None:
            result['AsyncId'] = self.async_id

        if self.context_shrink is not None:
            result['Context'] = self.context_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncId') is not None:
            self.async_id = m.get('AsyncId')

        if m.get('Context') is not None:
            self.context_shrink = m.get('Context')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

