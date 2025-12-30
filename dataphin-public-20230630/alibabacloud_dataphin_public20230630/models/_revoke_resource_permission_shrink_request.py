# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeResourcePermissionShrinkRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        revoke_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.revoke_command_shrink = revoke_command_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.revoke_command_shrink is not None:
            result['RevokeCommand'] = self.revoke_command_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RevokeCommand') is not None:
            self.revoke_command_shrink = m.get('RevokeCommand')

        return self

