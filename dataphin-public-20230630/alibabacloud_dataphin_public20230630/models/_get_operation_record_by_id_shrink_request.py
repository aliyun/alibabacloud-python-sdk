# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOperationRecordByIdShrinkRequest(DaraModel):
    def __init__(
        self,
        detail_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.detail_command_shrink = detail_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_command_shrink is not None:
            result['DetailCommand'] = self.detail_command_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailCommand') is not None:
            self.detail_command_shrink = m.get('DetailCommand')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

