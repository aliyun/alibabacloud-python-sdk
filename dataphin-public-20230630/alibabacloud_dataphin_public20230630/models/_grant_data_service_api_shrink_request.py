# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantDataServiceApiShrinkRequest(DaraModel):
    def __init__(
        self,
        grant_command_shrink: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.grant_command_shrink = grant_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_command_shrink is not None:
            result['GrantCommand'] = self.grant_command_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantCommand') is not None:
            self.grant_command_shrink = m.get('GrantCommand')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

