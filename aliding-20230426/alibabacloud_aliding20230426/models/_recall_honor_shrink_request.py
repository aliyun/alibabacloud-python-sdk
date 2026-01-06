# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecallHonorShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        honor_id: str = None,
        org_id: int = None,
        user_id: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.honor_id = honor_id
        # This parameter is required.
        self.org_id = org_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.honor_id is not None:
            result['honorId'] = self.honor_id

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('honorId') is not None:
            self.honor_id = m.get('honorId')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

