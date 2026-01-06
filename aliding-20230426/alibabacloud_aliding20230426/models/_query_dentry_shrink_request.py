# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDentryShrinkRequest(DaraModel):
    def __init__(
        self,
        dentry_id: str = None,
        include_space: bool = None,
        space_id: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.dentry_id = dentry_id
        self.include_space = include_space
        # This parameter is required.
        self.space_id = space_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_id is not None:
            result['DentryId'] = self.dentry_id

        if self.include_space is not None:
            result['IncludeSpace'] = self.include_space

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('IncludeSpace') is not None:
            self.include_space = m.get('IncludeSpace')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

