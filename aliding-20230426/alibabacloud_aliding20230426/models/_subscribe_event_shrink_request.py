# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubscribeEventShrinkRequest(DaraModel):
    def __init__(
        self,
        scope: str = None,
        scope_id: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.scope = scope
        # This parameter is required.
        self.scope_id = scope_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope is not None:
            result['Scope'] = self.scope

        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

