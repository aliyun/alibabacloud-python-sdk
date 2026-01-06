# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchMainOrgShrinkRequest(DaraModel):
    def __init__(
        self,
        target_org_id: int = None,
        tenant_context_shrink: str = None,
    ):
        self.target_org_id = target_org_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_org_id is not None:
            result['TargetOrgId'] = self.target_org_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetOrgId') is not None:
            self.target_org_id = m.get('TargetOrgId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

