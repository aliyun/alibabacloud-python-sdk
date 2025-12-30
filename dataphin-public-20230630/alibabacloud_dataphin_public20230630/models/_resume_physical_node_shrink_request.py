# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumePhysicalNodeShrinkRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        resume_command_shrink: str = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.resume_command_shrink = resume_command_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.resume_command_shrink is not None:
            result['ResumeCommand'] = self.resume_command_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ResumeCommand') is not None:
            self.resume_command_shrink = m.get('ResumeCommand')

        return self

