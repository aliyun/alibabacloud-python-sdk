# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRelatedWorkspacesShrinkRequest(DaraModel):
    def __init__(
        self,
        include_recent: bool = None,
        tenant_context_shrink: str = None,
    ):
        self.include_recent = include_recent
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_recent is not None:
            result['IncludeRecent'] = self.include_recent

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeRecent') is not None:
            self.include_recent = m.get('IncludeRecent')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

