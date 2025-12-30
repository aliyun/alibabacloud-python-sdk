# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNodeSupplementShrinkRequest(DaraModel):
    def __init__(
        self,
        create_command_shrink: str = None,
        env: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command_shrink = create_command_shrink
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command_shrink is not None:
            result['CreateCommand'] = self.create_command_shrink

        if self.env is not None:
            result['Env'] = self.env

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            self.create_command_shrink = m.get('CreateCommand')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

